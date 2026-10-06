import re

# Comprehensive list of technical and professional skills
COMMON_SKILLS = [
    # Languages
    "python", "java", "c++", "c#", "c", "javascript", "typescript", "golang", "go", "rust", "ruby", "php", "swift", "kotlin", "scala", "r", "dart", "matlab", "bash", "shell", "powershell",
    
    # Web & Frameworks
    "html", "css", "html5", "css3", "sass", "react", "react.js", "next.js", "vue", "vue.js", "angular", "node.js", "express", "express.js", "django", "flask", "fastapi", "spring", "spring boot", "asp.net", "laravel", "tailwind", "bootstrap", "graphql", "rest api", "restful api",
    
    # Databases & Caches
    "sql", "nosql", "mysql", "postgresql", "postgres", "sqlite", "mongodb", "redis", "elasticsearch", "cassandra", "dynamodb", "oracle", "mariadb", "firebase", "supabase",
    
    # AI / ML / Data
    "machine learning", "deep learning", "nlp", "computer vision", "artificial intelligence", "generative ai", "llm", "large language models", "prompt engineering", "langchain", "llamaindex", "huggingface", "pytorch", "tensorflow", "keras", "scikit-learn", "pandas", "numpy", "scipy", "data analysis", "data science", "data engineering", "data visualization", "matplotlib", "seaborn", "tableau", "power bi",
    
    # Cloud & DevOps
    "aws", "azure", "gcp", "google cloud", "docker", "kubernetes", "k8s", "terraform", "ansible", "jenkins", "github actions", "gitlab ci", "ci/cd", "linux", "unix", "nginx", "apache", "serverless",
    
    # Tools & Methodologies
    "git", "github", "gitlab", "bitbucket", "jira", "confluence", "agile", "scrum", "kanban", "microservices", "system design", "oop", "object-oriented programming", "unit testing", "pytest", "jest",
    
    # Soft & Management
    "problem solving", "communication", "teamwork", "leadership", "time management", "critical thinking", "project management", "collaboration"
]

def extract_skills(text: str) -> list:
    """
    Extracts skills from text using robust regex keyword matching.
    Lightweight, ultra-fast, and works across any environment without heavy dependencies.
    """
    if not text:
        return []
        
    text_lower = text.lower()
    extracted = set()
    
    # Match against skill dictionary
    for skill in COMMON_SKILLS:
        pattern = r'(?<![a-zA-Z0-9_])' + re.escape(skill) + r'(?![a-zA-Z0-9_])'
        if re.search(pattern, text_lower):
            # Formatted display naming
            if skill.lower() in ["aws", "gcp", "sql", "nlp", "ai", "ml", "llm", "ci/cd", "k8s", "oop", "api", "rest api"]:
                extracted.add(skill.upper())
            elif skill.lower() in ["javascript", "typescript", "postgresql", "mongodb", "fastapi", "scikit-learn", "github", "gitlab", "power bi"]:
                display_names = {
                    "javascript": "JavaScript", "typescript": "TypeScript", "postgresql": "PostgreSQL",
                    "mongodb": "MongoDB", "fastapi": "FastAPI", "scikit-learn": "Scikit-Learn",
                    "github": "GitHub", "gitlab": "GitLab", "power bi": "Power BI"
                }
                extracted.add(display_names.get(skill.lower(), skill.title()))
            else:
                extracted.add(skill.title())
            
    return sorted(list(extracted))
