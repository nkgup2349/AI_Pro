# Candidate Ranking ML Project

## Overview

This project ranks candidates based on their suitability for a job by processing and analyzing input data from a JSON file. It uses Natural Language Processing (NLP) techniques with SpaCy, regular expressions, and Python to extract, compare, and score candidate profiles against job descriptions.

## Features

- Input: JSON file containing candidate profiles and job descriptions.
- NLP-based skill extraction from job descriptions.
- Matching candidate skills with required skills.
- Scoring system based on:
  - Skill match percentage
  - Offered package vs. expected salary
  - Additional configurable criteria
- Output: JSON file with candidates ranked from best to least suitable.


## 🛠 Tech Stack

- Python  
- SpaCy  
- Regular Expressions  
- Pandas  
- JSON  



## Input JSON Format

```json
{
  "resumes": [
    {
      "id": "80112",
      "resume": "resumes/938390e9c09b344edb9ecc004997b2eb.pdf",
      "firstName": "Simmi",
      "middleName": null,
      "lastName": "Kumari",
      "dateOfBirth": "1995-01-16",
      "email": "user@gmail.com",
      "phoneNumber": "1234567890",
      "alternatePhoneNumber": "",
      "gender": "Female",
      "highestQualification": "MBA",
      "skills": "Networking and relationship building,key tool of recruitment,Active listening,Communication skills,Time management,",
      "currentCompany": "PDAG",
      "profile": "HR Recruiter",
      "currentDesignation": "HR Associate",
      "totalExperience": "2",
      "relevantExperience": "2",
      "currentLocation": "Ranchi City",
      "preferredLocation": ["Pune,Noida"],
      "currentCTC": "2.6",
      "expectedCTC": "4",
      "noticePeriod": "0",
      "lastWorkingDay": "2024-03-30",
      "holdingAnyOffer": null,
      "interestedRole": "Permanent",
      "vendorName": null,
      "languagesKnown": ["English and Hindi"],
      "createdAt": "2024-04-08T10:11:33.703Z",
      "updatedAt": "2025-02-11T11:05:48.618Z",
      "candidateId": 6108
    },
    {
      "id": "70202",
      "resume": "resumes/6781895ecab16ed1f7e240321a1eefbd.pdf",
      "firstName": "Sushma",
      "middleName": null,
      "lastName": "Gupta",
      "dateOfBirth": "1980-10-23",
      "email": "user@gmail.com",
      "phoneNumber": "12345667890",
      "alternatePhoneNumber": "1234567890",
      "gender": "Female",
      "highestQualification": "B.com",
      "skills": "Screening,Recruiting,Database",
      "currentCompany": "Ahom Technologies PVT.LTD",
      "profile": "Hr Recruiter",
      "currentDesignation": "Hr Recruiter",
      "totalExperience": "2",
      "relevantExperience": "2",
      "currentLocation": "Siliguri",
      "preferredLocation": ["Siliguri"],
      "currentCTC": "0.84",
      "expectedCTC": "1.50",
      "noticePeriod": "Immediate joiner",
      "lastWorkingDay": "2024-04-19",
      "holdingAnyOffer": "Yes",
      "interestedRole": "Both",
      "vendorName": null,
      "languagesKnown": ["Hindi, English, Bengali"],
      "createdAt": "2024-04-28T10:48:04.112Z",
      "updatedAt": "2025-02-11T11:05:49.956Z",
      "candidateId": 9816
    },
  ],
  "job_description": "Job Title: HR Recruiter (IT / Non-IT)\nJob Location: Greater Noida West\nYears of Experience: 1.5 - 3 Years\nBudget: Up to ₹3.5 LPA\nJob Type: Full-time, Permanent Role\n\nKey Responsibilities:\n1. Partner with client-side hiring managers to understand staffing needs.\n2. Review and align job descriptions with ideal candidate profiles.\n3. Source candidates using job portals, social media, and internal databases.\n4. Conduct telephonic/video screening and assess relevant experience.\n5. Coordinate interviews between shortlisted candidates and hiring managers.\n6. Maintain timely updates and follow-ups throughout the hiring process.\n7. Act as a liaison between candidates and clients until onboarding.\n8. Build a pipeline of qualified candidates for recurring requirements.\n\nRequirements and Skills:\n- 1.5–3 years of hands-on recruitment experience (IT/Non-IT).\n- Strong in sourcing, screening, interview coordination, and onboarding.\n- Familiar with ATS tools, MS Office, and Google Workspace (Docs, Sheets, Gmail).\n- Excellent verbal and written communication in English and Hindi.\n- Immediate joiners or candidates with up to 15 days notice preferred.\n- Comfortable with onsite work at Greater Noida West.\n\nPreferred Traits:\n- Strong client and candidate management skills.\n- Confident in handling high-volume hiring with quick TAT.\n- Ability to manage Excel-based trackers or dashboards.\n- Open to permanent roles and long-term growth."
}
```

##Output JSON Format

```json
[
  {
    "candidateId": 6108,
    "name": "John Doe",
    "score": 52
  },
{
    "candidateId": 9816,
    "name": "John Doe",
    "score":47
  },
]



```

## 🚀 How to Run

 Clone the repository  
```
git clone https://github.com/nkgup2349/AI_Pro.git
```

Install dependencies
```
pip install -r requirements.txt
```

# Run the Streamlit app

```
python main.py
```


## 🧱 Project Structure
```
.
├── App.py                     # Main Streamlit application
├── candidate_sample.json      # Sample input data
├── requirements.txt           # Dependencies
└── README.md                  # Documentation

```

##💡 Future Improvements

Integration with PDF/Docx parsers for resume extraction

Admin dashboard for managing job postings and uploads

MongoDB integration for persistent candidate storage

More refined NLP techniques for deeper semantic analysis

