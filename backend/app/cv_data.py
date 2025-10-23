from .models import CVData

# Customize this data with your actual CV information
CV_DATA = CVData(
    personal_info={
        "name": "Prosper Mambambo",
        "title": "Software Developer & AI Enthusiast",
        "location": "Observatory, Cape Town",
        "email": "pmambambo2@gmail.com",
        "phone": "+27 (0) 81 412 0964",
        "summary": """With a passion for making a lasting impact on the industry, I am a tech
        enthusiast and software prodigy. Combining extensive leadership experience, project 
        management skills, and a delightful sense of humour, I bring significant value to any 
        company, alongside unwavering dedication and drive for personal and professional growth."""
    },
    
    experience=[
        {
            "company": "Derivco",
            "role": "Software Developer",
            "period": "Feb 2025 - Present",
            "location": "Cape Town, South Africa",
            "responsibilities": [
                "Designed and implemented AI-driven workflows using N8N and context engineering to automate long, repetitive business processes within the organisation",
                "Leveraged AI agents to reduce manual workload, improve efficiency, and accelerate decision-making as part of the R&D Department",
                "Developed custom MCP servers to empower AI agents with dynamic access to company web services, enabling secure filtering, data retrieval, and workflow automation",
                "Built, tested, maintained and deployed RESTful APIs in C#"
            ],
            "technologies": ["C#", "N8N", "AI Agents", "MCP Servers", "RESTful APIs", "Workflow Automation"]
        },
        {
            "company": "Teamgeek",
            "role": "Software Engineer",
            "period": "Dec 2024 - Jan 2025",
            "location": "South Africa",
            "responsibilities": [
                "Contributed to the development and maintenance of features on the Yoco South Africa website during the internship",
                "Utilized modern web technologies for frontend development"
            ],
            "technologies": ["Tailwind CSS", "TypeScript", "Next.js"]
        },
        {
            "company": "SMS Portal",
            "role": "Software Engineering Intern",
            "period": "Nov 2024",
            "location": "South Africa",
            "responsibilities": [
                "Worked on optimizing company systems by addressing performance bottlenecks and memory inefficiencies",
                "Successfully reduced the software's RAM consumption from 8GB to just 1MB, while preserving constant-time efficiency for search and insertion operations within the algorithm",
                "Achieved this by redesigning data structures and implementing optimized algorithms",
                "This improvement significantly enhanced system stability, scalability, and cost-effectiveness"
            ],
            "technologies": ["C#", "Algorithm Optimization", "Data Structures"]
        },
        {
            "company": "Mohara Ventures",
            "role": "Software Engineering Intern",
            "period": "Jun 2023 - Jul 2023",
            "location": "South Africa",
            "responsibilities": [
                "Built and tested frontend applications for the company using React",
                "Focused on creating user-friendly interfaces, making sure the apps worked smoothly across devices",
                "Connected frontend applications with backend systems"
            ],
            "technologies": ["React", "Frontend Development", "Cross-device Compatibility"]
        },
        {
            "company": "Iinet",
            "role": "Software Engineer",
            "period": "Jan 2021 - May 2023",
            "location": "Australia",
            "responsibilities": [
                "Built internal scripts with Python and Node to detect and resolve fibre network issues via NBN APIs",
                "Used Postman, Git and Docker for debugging and deployment",
                "Improved reliability and automated parts of the support process"
            ],
            "technologies": ["Python", "Node.js", "NBN APIs", "Postman", "Git", "Docker"]
        }
    ],
    
    education=[
        {
            "institution": "University of Cape Town",
            "degree": "B.Sc. Honours in Computer Science",
            "period": "2024",
            "location": "Cape Town, South Africa",
            "achievements": [
                "Completed Honours degree in Computer Science",
                "Advanced coursework in computer science theory and practice"
            ]
        },
        {
            "institution": "University of Cape Town",
            "degree": "B.Sc. Business Computing",
            "period": "2021 - 2023",
            "location": "Cape Town, South Africa",
            "achievements": [
                "Graduated with Bachelor of Science in Business Computing",
                "Combined technical skills with business acumen",
                "Strong foundation in both computing and business principles"
            ]
        }
    ],
    
    skills={
        "programming_languages": [
            "Java", "C#", "Python", "JavaScript", "TypeScript"
        ],
        "frontend": [
            "React", "Tailwind CSS", "HTML", "CSS", "Bootstrap"
        ],
        "backend_and_frameworks": [
            ".NET", "Django"
        ],
        "databases": [
            "MongoDB", "SQL"
        ],
        "devops_and_tools": [
            "Docker", "Git", "Bitbucket", "Jira"
        ],
        "ai_and_automation": [
            "LangChain", "Mistral", "N8N", "AI Agents", "MCP Servers"
        ],
        "testing_and_qa": [
            "Automated Testing", "ISTQB Certified"
        ],
        "cloud": [
            "Microsoft Azure", "AZ-900 Certified", "AI-900 Certified"
        ]
    },
    
    projects=[
        {
            "name": "CV Analyzer Application",
            "description": "Full-stack application for analyzing CVs and generating cover letters using AI",
            "technologies": ["C#", ".NET", "React", "TypeScript", "OpenAI API"],
            "features": [
                "PDF text extraction and analysis",
                "AI-powered cover letter generation",
                "Modern React frontend with responsive design",
                "RESTful API with .NET backend"
            ],
            "github": "https://github.com/yourusername/cv-analyzer"  # Update with actual link
        },
        {
            "name": "Interactive CV Chatbot",
            "description": "AI-powered chatbot that answers questions about professional background",
            "technologies": ["Python", "FastAPI", "LangChain", "React", "OpenAI"],
            "features": [
                "Real-time chat interface",
                "RAG-based question answering",
                "Professional deployment on Render",
                "WebSocket communication"
            ],
            "status": "In Development"
        },
        {
            "name": "SwiftTruck Application",  # Based on directory structure seen earlier
            "description": "Mobile application for logistics and transportation management",
            "technologies": ["React Native", "Node.js", "MongoDB"],
            "features": [
                "Real-time tracking",
                "User management system",
                "Mobile-responsive design"
            ]
        }
    ],
    
    achievements=[
        "Successfully delivered multiple full-stack applications in production",
        "Implemented AI-powered features using modern LLM technologies",
        "Demonstrated expertise in both frontend and backend development",
        "Experience with cloud deployment and DevOps practices",
        "Strong problem-solving skills and ability to learn new technologies quickly"
    ],
    
    certifications=[
        "Microsoft Azure Fundamentals (AZ-900)",
        "Microsoft Azure AI Fundamentals (AI-900)",
        "ISTQB Certified - Testing & QA"
    ]
)

# Additional context for the AI agent
INTERVIEW_CONTEXT = """
You are an AI assistant representing Prosper Mambambo in a conversational interview setting. 
You should:

1. Answer questions as if you are Prosper, using first-person language
2. Be professional but personable
3. Highlight relevant experience and skills based on the question
4. Provide specific examples when discussing projects or achievements
5. Show enthusiasm for technology and continuous learning
6. Be honest about areas for growth while emphasizing strengths
7. Connect experiences to potential value for employers

Key talking points:
- Strong technical foundation in both frontend and backend development
- Experience with AI/ML technologies and modern frameworks
- Proven ability to deliver complete applications from concept to deployment
- Collaborative team player with good communication skills
- Passionate about solving problems through technology
"""