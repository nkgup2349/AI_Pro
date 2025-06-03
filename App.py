import nltk
import spacy
nltk.download('stopwords')
custom_nlp = spacy.load('en_core_web_sm')
import re
import json 
import os
from datetime import datetime

def extract_languages(text):
    languages = ["english", "hindi", "telugu", "tamil", "bengali", "marathi", "kannada"]
    found_languages = [lang for lang in languages if lang in text.lower()]
    return list(set(found_languages)) if found_languages else None

def extract_role(text):
    match = re.search(r"Job Title[:\-]?\s*(.*)", text, re.IGNORECASE)
    return match.group(1).strip() if match else None

def extract_location(text):
    match = re.search(r"Job Location[:\-]?\s*(.*)", text, re.IGNORECASE)
    return match.group(1).strip() if match else None

def extract_experience(text):
    match = re.search(r'(\d+(\.\d+)?)\s*(to|-)\s*(\d+(\.\d+)?)\s*years', text.lower())
    if match:
        return float(match.group(1)), float(match.group(4))
    return None, None

def extract_budget(text):
    match = re.search(r'₹?(\d+(\.\d+)?)\s*(LPA|lpa|lakhs)', text)
    if match:
        return float(match.group(1))
def extract_skills(text):
    text_lower = text.lower()
    keywords = [
        "sourcing", "networking and relationship building", "drive", "docs", "database",
        "screening", "recruiting", "communication skills", "time management", "client handling",
        "candidate handling", "recruitment", "active listening", "hiring", "interviewing",
        "onboarding", "hr operations", "employee relations", "gmail", "sheets", "ms office",
        "word", "staffing", "excel", "outlook", "powerpoint", "access", "interview coordination",
        "candidate management" , "client management","management" ,"tat"
        "google workspace", "ats tools"
    ]
    found_skills = [skill for skill in keywords if skill in text_lower]
    return list(set(found_skills)) if found_skills else None

def extract_notice(text):
    text = text.lower()
    patterns = [
        r'max(?:imum)?\s*(\d{1,3})\s*days?',
        r'up to\s*(\d{1,3})\s*days?',
        r'0\s*(?:to|-)\s*(\d{1,3})\s*days?',
        r'within\s*(\d{1,3})\s*days?',
        r'notice period.*?(\d{1,3})\s*days?',
        r'(\d{1,3})\s*days?\s*notice'
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return f"{int(match.group(1))} days"
    if "immediate" in text:
        return "Immediate"
    return None

def extract_jd_fields(jd_text):
    doc = jd_text  ; 
    return {
        "role": extract_role(doc),
        "location": extract_location(doc),
        "min_experience": extract_experience(jd_text)[0],
        "max_experience": extract_experience(jd_text)[1],
        "skills_required": extract_skills(jd_text),
        "budget_lpa": extract_budget(jd_text),
        "notice_period": extract_notice(jd_text),
        "language" : extract_languages(jd_text)
    }




def calculate_resume_score(resume, jd):
    score = 0
    total = 0
    # 1. Skills Match

    total += 40

    resume_skills = [skill.lower() for skill in resume['skills']]
    jd_skills = [skill.lower() for skill in jd['skills_required']]
    matched_skills = list(set(resume_skills) & set(jd_skills))
    skill_score = (len(matched_skills) / len(jd_skills)) * 40
    score += skill_score

    # 2. Experience Match
    total += 30
    min_exp = jd.get('min_experience', 0)   # default 0 if missing
    max_exp = jd.get('max_experience', float('inf'))  # default very large if missing

    if min_exp <= float(resume['relevantExperience']) <= max_exp:
        score += 30
    elif abs(resume['relevantExperience'] - min_exp) <= 1:
        score += 20

    # 3. Location Match

    city_aliases = {
    "bangalore": ["bengaluru" , "bangaluru"],
    "mumbai": ["navi mumbai", "bombay"],
    "delhi": ["new delhi", "delhi ncr"],
    "hyderabad": ["cyberabad"],
    "chennai": ["madras"],
    "noida": ["Greater Noida" , "noida city"],
    "gurugram" : ["gurgaon" , "cyberhub"]
    }
    total += 10
    job_loc = jd['location'].strip().lower()
    aliases = city_aliases.get(job_loc, []) + [job_loc]
    for loc in resume.get('preferredLocation', []):
        loc_clean = loc.strip().lower()
        for alias in aliases:
            if alias in loc_clean:
                score += 10
                break
        else:
            continue
        break

    # 4. Notice Period
    total += 10
    if jd['notice_period'] == 'immediate':
        if resume['noticePeriod'] in ['immediate', '0', '0 days']:
            score += 10
    else:
        try:
            jd_days = int(''.join(filter(str.isdigit, jd['notice_period'])))
            resume_days = int(''.join(filter(str.isdigit, resume['noticePeriod'])))
            if 0 <= resume_days <= jd_days:
                score += 10
        except ValueError:
            pass

    # 5. Language Match
    total += 10
    resume_langs = set(lang.lower() for lang in resume.get('languagesKnown', [])) 
    jd_langs = set(lang.lower() for lang in jd.get('language_required', []))

    if jd_langs:  
        matched_langs = resume_langs & jd_langs
        lang_score = (len(matched_langs) / len(jd_langs)) * 10
        score += lang_score
    else:
        score += 10


    #budget Match
    total += 15
    try:
        required = float(resume.get('expectedCTC', 0))
        budget = float(jd.get('budget_lpa', 0))
        if budget >= required and required > 0:
            score += 15
    except ValueError:
        pass

    result = float(score / total)*100 
    return result;


def run():
    with open('candidate_sample.json', 'r') as f:
        resume_data = json.load(f)
    if resume_data:
        job_desc = resume_data.get("job_description", "")
        print(job_desc)
        resume= resume_data.get("resumes", [])
        jd = extract_jd_fields(job_desc)
        print(jd)
        sdata = []
        for i in resume:
            num =  calculate_resume_score(i , jd)
            name_parts = [i.get("firstName"), i.get("middleName"), i.get("lastName")]
            score_val = round(num, 3)
            name = " ".join(part for part in name_parts if part) 
            id = i['candidateId']
            
            sdata.append({
                "candidateId": id,
                "name": name,
                "score": score_val
            })   
        
        data = sorted(sdata, key=lambda x: x['score'], reverse=True)
        os.makedirs("result", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"result_{timestamp}.json"
        file_path = os.path.join("result", filename)

        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
    else:
        print("No Resume data found")
run()