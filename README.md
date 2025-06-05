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

## Input JSON Format

```json
{
  "candidates": [
    {
      "name": "John Doe",
      "skills": ["python", "ml", "nlp"],
      "expected_salary": 70000
    },
    {
      "name": "Jane Smith",
      "skills": ["java", "spring", "ml"],
      "expected_salary": 80000
    }
  ],
  "job_description": "We are looking for a candidate with skills in python, ml, and nlp. Offered package is 75000."
}.
```

##Output JSON Format

```json
{
  "ranked_candidates": [
    {
      "name": "John Doe",
      "score": 92
    },
    {
      "name": "Jane Smith",
      "score": 65
    }
  ]
}
