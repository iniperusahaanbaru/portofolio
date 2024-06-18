import streamlit as st
from pyairtable import Api
from requests.exceptions import HTTPError
import time
from PIL import Image
import base64
import os
from streamlit_pdf_viewer import pdf_viewer
# Set page configuration


# Define skills with descriptions
technical_skills = {
    "Python Programming": "Expert at using the Python language to create programs, automate tasks, and build applications.",
    "AI API Integration": "Knows how to connect to AI systems (like ChatGPT) to use their advanced capabilities for analyzing data and making decisions.",
    "Selenium": "Skilled at automating tasks in web browsers, like collecting data from websites or running tests.",
    "MySQL": "Can manage and work with databases to store and organize information.",
    "Google Cloud": "Experienced in using Google's cloud services for reliable and secure storage and computing.",
    "Google Sheets API": "Can connect programs to Google Sheets for tasks like updating spreadsheets automatically.",
    "PowerPoint": "Creates professional presentations to share information effectively.",
    "Firestore Database": "Can work with a special kind of database designed for real-time data updates.",
    "Google Storage API": "Can store and access data in Google's cloud storage.",
    "Basic HTML and CSS for Streamlit": "Uses basic web design skills to make apps built with Streamlit look nice and work well.",
    "Microsoft Word": "Can arrange and write and modified document in propesional format"
}

advanced_skills = {
    "Data Processing": "Highly skilled at cleaning, organizing, and preparing data for analysis.",
    "Automation Engineering": "Creates systems that automate complex tasks, saving time and effort.",
    "Prompt Engineering": "Expert at crafting instructions to get the best results out of AI systems.",
    "GUI Creation": "Builds user-friendly interfaces for programs.",
    "Web Scraping": "Collects information from websites automatically.",
    "Database Management": "Maintains and secures databases.",
    "Business Analysis": "Analyzes business needs and creates plans to address them.",
    "Presentation Design": "Creates presentations that are both informative and visually appealing.",
    "Financial Analysis": "Analyzes financial data to understand a company's performance.",
    "Product Design": "Designs products with the user in mind.",
    "Basic Website Creation": "Can create simple, user-friendly websites."
}
soft_skills = {
    "Attention to Detail": "Works carefully to avoid mistakes.",
    "Creative Problem Solving": "Finds innovative solutions to challenges.",
    "Out-of-the-box Thinking": "Finds creative solutions to problems using AI.",
    "Error Minimization": "Takes steps to make sure data is accurate and reliable.",
    "Effective Communication": "Can explain complex ideas in simple terms.",
    "Proposal Writing": "Creates clear and convincing proposals.",
    "Leadership": "Can guide teams and projects effectively.",
    "Teamwork": "Works well with others to achieve goals.",
    "Tech Savviness": "Stays informed on current technology trends and industry developments." 
}

projects = {
    "Automate Excel Data Merging": {
        "skills": ["Python Programming", "Attention to Detail", "Data Processing", "Automation Engineering"],
        "goal_description": "To automate the process of combining information from different tabs in an Excel file into a single tab, ensuring all relevant data is merged accurately and efficiently.",
        "how_it_works": {
            "Load Excel File": "The script loads the Excel file containing the data to be merged.",
            "Read Sheets": "It reads the specified sheets from the Excel file into separate DataFrames.",
            "Merge Data": "The script merges the data from different sheets based on a common column (email addresses). Additional information from corresponding columns is appended to the base sheet.",
            "Save Merged Data": "The final merged data is saved into new Excel files for easy access and further use."
        },
        "technical_skills": {
            "Python Programming": "The main programming language used for developing the script."
        },
        "advanced_skills": {
            "Data Processing": "Techniques for handling and transforming data to ensure accurate merging, utilizing multiple tools effectively.",
            "Automation Engineering": "Developing scripts and processes to automate the data merging from multiple tabs, enhancing efficiency and reducing manual work."
        },
        "soft_skills": {
            "Attention to Detail": "Ensures all data is accurately merged without errors or omissions."
        },
        "image": "automate_excel.png",  # Path to the image file
        "video": "automate_excel.mp4",  # Path to the video file
        "URL": None
    },

    "Automate Web Browser Startup on Dual Monitor": {
        "skills": ["Python Programming", "Automation Engineering"],
        "goal_description": "To automate the process of starting web browsers on specific monitors in a dual-monitor setup, ensuring that the cashier's URL remains on the main monitor and the customer's URL is displayed on the secondary monitor.",
        "how_it_works": {
            "Open Browser Windows": "The script uses subprocess to open new browser windows with specified URLs.",
            "Detect Open Windows": "It uses pygetwindow to get a list of all open windows and identify the ones containing the specified URLs.",
            "Move Windows to Specific Monitors": "The script defines a function to move the detected windows to the specified monitors. It restores and maximizes the windows if they are minimized or maximized. The window for the cashier remains on the main monitor, while the window for the customer is moved to the secondary monitor."
        },
        "technical_skills": {
            "Python Programming": "The main programming language used for developing the script."
        },
        "advanced_skills": {
            "Automation Engineering": "Developing scripts and processes to automate the startup and positioning of web browsers, enhancing efficiency and reducing manual work."
        },
        "soft_skills": "None",
        "image": "automate_browser.png",  # Path to the image file if available
        "video": "automate_browser.mp4",  # Path to the video file if available
        "URL": None
    },

    "Extract Parliamentary Results from PDF to CSV": {
        "skills": ["Python Programming", "Automation Engineering", "Data Extraction", "AI API Integration", "Out-of-the-box Thinking", "Error Minimization", "GUI Creation","Tech Savviness"],
        "goal_description": "To automate the extraction and processing of parliamentary election results from PDF files, converting the data into a structured CSV format for research purposes.",
        "how_it_works": {
            "Select PDF Files": "Users select multiple PDF files using a file dialog within the application.",
            "Extract Text from PDFs": "The application uses pdfplumber to extract text from each page of the selected PDFs.",
            "Process Data with AI": "The extracted text is sent to an AI model (Claude-3-haiku) for analysis. The AI processes the text to extract relevant data fields, ensuring the data is organized according to predefined headers.",
            "Generate and Save CSV Files": "The processed data is structured into a DataFrame and saved to a CSV file. If a CSV file already exists, the new data is appended to the existing file, ensuring all data is consolidated."
        },
        "technical_skills": {
            "Python Programming": "The main programming language used for developing the script.",
            "AI API Integration": "Utilizing AI API from Anthropic to process and analyze extracted text data."
        },
        "advanced_skills": {
            "Automation Engineering": "Developing scripts and processes to automate the data extraction and structuring from PDF files, enhancing efficiency and reducing manual work.",
            "Tech Savviness": "Use the most recent ai technology which is faster to make and easier to use",
            "Prompt Engineering": "Designing effective prompts for the AI model to accurately extract and structure data.",
            "GUI Creation": "Developing a user-friendly graphical interface for the application."
        },
        "soft_skills": {
            "Out-of-the-box Thinking": "Using AI to solve complicated problems more accurately and faster than traditional methods.",
            "Error Minimization": "Implementing meticulous methods to drastically reduce errors in data extraction and processing, ensuring reliability and integrity."
        },
        "image": "extract_parliamentary_results.png",  # Path to the image file if available
        "video": "extract_parliamentary_results.mp4",  # Path to the video file if available
        "URL": None
    },

    "SEC Data Scraping and Processing": {
        "skills": ["Python Programming", "Selenium", "Automation Engineering", "Data Processing", "Attention to Detail", "Error Minimization","Web Scraping"],
        "goal_description": "To automate the extraction of company data from the SEC website and organize it into structured Excel files for analysis.",
        "how_it_works": {
            "Load SEC Website": "The script uses Selenium to navigate to the SEC EDGAR search page.",
            "Input Search Criteria": "It inputs company codes or names into the search bar and submits the search.",
            "Extract Data": "The script uses BeautifulSoup to parse the page and extract relevant company information, including addresses and phone numbers.",
            "Process and Save Data": "Extracted data is processed and saved into a structured Excel file. If an Excel file already exists, the new data is appended to the existing file, ensuring all data is consolidated."
        },
        "technical_skills": {
            "Python Programming": "The main programming language used for developing the script.",
            "Selenium": "Utilizing Selenium for automating web browser interactions to facilitate web scraping and testing."
        },
        "advanced_skills": {
            "Automation Engineering": "Developing scripts and processes to automate the data extraction from the SEC website, enhancing efficiency and reducing manual work.",
            "Data Processing": "Techniques for handling and transforming extracted data to ensure accuracy and consistency.",
            "Web Scraping": "Expert in extracting data from websites using advanced techniques with tools like Selenium and BeautifulSoup."
        },
        "soft_skills": {
            "Attention to Detail": "Ensuring meticulous accuracy and thoroughness in all tasks, significantly reducing the potential for errors.",
            "Error Minimization": "Implementing meticulous methods to drastically reduce errors in data extraction and processing, ensuring reliability and integrity."
        },
        "image": "sec_scrap.png",  # Path to the image file if available
        "video": "sec_scrap.mp4",  # Path to the video file if available
        "URL": None
    },
    "Automate Report Generation": {
        "skills": ["Python Programming", "Data Processing" ,"Automation Engineering", "GUI Creation", "Attention to Detail", "Error Minimization","Tech Savviness"],
        "goal_description": "To automate the processing of Excel data and generate comprehensive reports, enhancing efficiency and accuracy in data analysis and presentation.",
        "how_it_works": {
            "Upload and Read Excel File": "Users upload an Excel file, which is read into the application using pandas.",
            "Data Analysis and Visualization": "The application analyzes the data, generates summary statistics, and creates visualizations such as pie charts to represent the data.",
            "Generate and Save Report": "The analyzed data and visualizations are compiled into a structured Word document, which is saved for further use and presentation. The process includes hashing for secure data handling."
        },
        "technical_skills": {
            "Python Programming": "The main programming language used for developing the script.",
        },
        "advanced_skills": {
            "Data Processing": "Techniques for handling and transforming data to ensure accurate analysis and visualization.",
            "Automation Engineering": "Developing scripts and processes to automate the data analysis and report generation, enhancing efficiency and reducing manual work.",
            "GUI Creation": "Developing a user-friendly graphical interface for the application.",
        },
        "soft_skills": {
            "Attention to Detail": "Ensuring meticulous accuracy and thoroughness in all tasks, significantly reducing the potential for errors.",
            "Error Minimization": "Implementing meticulous methods to drastically reduce errors in data processing and report generation, ensuring reliability and integrity.",
            "Tech Savviness": "Use the most recent ai technology which is faster to make and easier to use"
        },
        "image": None,  # Path to the image file if available
        "video": "excel_report.mp4",  # Path to the video file if available
        "URL": None
    },

    "AI Screenshot App": {
        "skills": ["Python Programming", "GUI Creation", "AI API Integration", "Attention to Detail", "Product Design","Tech Savviness"],
        "goal_description": "To create a screenshot tool that integrates with AI for providing detailed explanations based on the captured images and converting text to Excel format.",
        "how_it_works": {
            "Take Screenshot": "Users can take a screenshot of their screen using a custom snipping tool.",
            "Save and Display Screenshot": "The screenshot is saved and displayed within the application for further processing.",
            "AI Explanation": "Users can input text to get detailed explanations from an AI model based on the screenshot and the provided text input.",
            "Convert Text to Excel": "The tool can also convert the extracted information into an Excel format for further analysis."
        },
        "technical_skills": {
            "Python Programming": "The main programming language used for developing the application.",
            "AI API Integration": "Utilizing AI API to provide detailed explanations based on the screenshot.",
        },
        "advanced_skills": {
            "GUI Creation": "Developing a user-friendly graphical interface for the screenshot tool, enhancing user experience and interaction.",
            "Product Design": "Innovative and user-centric approach to designing multifunction screen-shoot app and integrating the most advance technology."
        },
        "soft_skills": {
            "Attention to Detail": "Ensuring meticulous accuracy and thoroughness in all tasks, significantly reducing the potential for errors.",
            "Tech Savviness": "Use the most recent ai technology to update an app that was use a lot but has no update"


        },
        "image": None,  # Path to the image file if available
        "video": "screenshot_tool.mp4",  # Path to the video file if available
        "URL": None
    },

    "Automate CV Analyzer with Google Sheets Integration": {
        "skills": ["Python Programming", "Google Sheets API", "Data Processing", "Automation Engineering", "Attention to Detail", "Error Minimization","Creative Problem Solving", "Product Design","GUI Creation"],
        "goal_description": "To create a tool that processes CVs and integrates the extracted data into Google Sheets, facilitating efficient data handling and analysis.",
        "how_it_works": {
            "Select PDF Files": "Users select multiple PDF files using a file dialog within the application.",
            "Extract Text from PDFs": "The application uses pdfplumber to extract text from each page of the selected PDFs.",
            "AI Analysis and Data Extraction": "The extracted text is analyzed by an AI model to extract relevant data fields, ensuring the data is organized according to predefined headers.",
            "Update Google Sheets": "The processed data is uploaded to a specified Google Sheets document for further analysis and use."
        },
        "technical_skills": {
            "Python Programming": "The main programming language used for developing the application.",
            "Google Sheets API": "Utilizing the Google Sheets API for integrating and automating spreadsheet tasks."
        },
        "advanced_skills": {
            "Data Processing": "Techniques for handling and transforming extracted data to ensure accuracy and consistency.",
            "Automation Engineering": "Developing scripts and processes to automate the data extraction and Google Sheets update, enhancing efficiency and reducing manual work.",
            "Product Design": "Deasign the app to be easy to used even for non tech user.",
            "GUI Creation": "Developing a user-friendly graphical interface for the screenshot tool, enhancing user experience and interaction.",

        },
        "soft_skills": {
            "Attention to Detail": "Ensuring meticulous accuracy and thoroughness in all tasks, significantly reducing the potential for errors.",
            "Error Minimization": "Implementing meticulous methods to drastically reduce errors in data processing and Google Sheets update, ensuring reliability and integrity.",
            "Creative Problem Solving": "Utilizing automation to solve repetitive and tedious task of reading cv manually and categorizing it",
            "Tech Savviness" : "Use the most advance technology to automate a hard solve problem that was hard to solve before it was widely availablexx`"
        },
        "image": None,  # Path to the image file if available
        "video": "pdf_processor.mp4",  # Path to the video file if available
        "URL": None
    },

    "Financial Report Analysis for PT Unilever Indonesia Tbk": {
        "skills": ["Business Analysis", "Data Processing", "Financial Analysis", "Attention to Detail", "Effective Communication","Microsoft Word"],
        "goal_description": "To conduct a comprehensive financial analysis of PT Unilever Indonesia Tbk using ratio analysis, vertical analysis, and horizontal analysis.",
        "how_it_works": {
            "Activity Ratios": "Analyze the effectiveness of resource utilization using metrics such as inventory turnover and days' sales in inventory.",
            "Solvency Ratios": "Evaluate the company's ability to meet long-term obligations using ratios such as liabilities to equity and interest coverage.",
            "Profitability Ratios": "Assess the company's ability to generate profit relative to its assets, equity, and sales.",
            "Liquidity Ratios": "Measure the company's ability to meet short-term obligations using current and quick ratios.",
            "Vertical Analysis": "Conduct vertical analysis to understand the proportion of various accounts within the financial statements.",
            "Horizontal Analysis": "Perform horizontal analysis to compare financial data over multiple periods, identifying trends and growth patterns."
        },
        "technical_skills": {
            "PowerPoint": "Creating detailed and informative presentations to communicate financial analysis findings."
        },
        "advanced_skills": {
            "Business Analysis": "Analyzing financial statements and extracting meaningful insights.",
            "Data Processing": "Handling and transforming financial data to perform accurate and insightful analysis.",
            "Financial Analysis": "Comprehensive analysis of financial statements using various ratios and techniques to extract meaningful insights."
        },
        "soft_skills": {
            "Attention to Detail": "Ensuring accuracy and thoroughness in financial analysis, minimizing the risk of errors.",
            "Effective Communication": "Clearly conveying the results and implications of financial analysis through well-structured reports and presentations.",
            "Proposal Writing": "Crafting detailed and persuasive proposals that effectively communicate project goals, methodologies, and anticipated impacts.",
            "Teamwork": "Collaborating effectively with team members to achieve common goals and deliver high-quality results."
        },
        "image": None,  # Path to the image file if available
        "video": None,  # Path to the video file if available
        "URL": "unilever_analysis.pdf"
    },
    ################################################################################################# BUSINESS PROPOSAL
    "Bu-Jet: AI Financial Management Tools Proposal": {
        "skills": ["Python Programming", "AI API Integration", "PowerPoint", "Attention to Detail", "Out-of-the-box Thinking", "Effective Communication", "Proposal Writing", "Creative Problem Solving", "Product Design"],
        "goal_description": "To develop a comprehensive proposal for an AI-powered financial management tool aimed at improving financial literacy and inclusion in Indonesia.",
        "how_it_works": {
            "Problem Statement": "Identify the low financial literacy (38%) in Indonesia and its impact on poor financial management among the populace.",
            "Solution Approach": "Propose Bu-Jet, an AI financial management tool that provides personalized financial analysis, budgeting, and spending alerts.",
            "Technical Use": "AI analyzes users' financial transactions, creates automatic budgets, and provides recommendations for financial improvement.",
            "Impact": "Demonstrate the positive impact of Bu-Jet on improving financial literacy and supporting Bank Indonesia's vision for financial inclusion."
        },
        "technical_skills": {
            "Python Programming": "Used for developing the core application logic and integrating with financial data sources.",
            "AI API Integration": "Utilizing AI APIs to provide personalized financial analysis and recommendations.",
            "PowerPoint": "Creating engaging and informative presentations to effectively communicate the proposal."
        },
        "advanced_skills": {
            "Business Analysis": "Analyzing the financial management needs in Indonesia and proposing effective solutions.",
            "Presentation Design": "Designing a compelling presentation to clearly convey the proposal and its benefits.",
            "Product Design": "Innovative and user-centric approach to designing the AI financial management tool, ensuring it meets user needs and enhances their experience."
        },
        "soft_skills": {
            "Attention to Detail": "Ensuring the proposal is meticulously crafted with accurate and relevant information.",
            "Out-of-the-box Thinking": "Innovative problem-solving to create a unique and effective financial management tool.",
            "Effective Communication": "Clearly conveying complex information in the proposal and presentation.",
            "Proposal Writing": "Crafting a detailed and persuasive business proposal that effectively communicates the project goals, methodologies, and anticipated impacts.",
            "Creative Problem Solving": "Utilizing creative approaches to tackle financial literacy challenges and develop effective solutions."
        },
        "image": None,  # Path to the image file if available
        "video": None,  # Path to the video file if available
        "URL": "bujet_proposal.pdf"
    },

    "Repair Me Business Proposal": {
        "skills": ["PowerPoint", "Business Analysis", "Presentation Design", "Attention to Detail", "Effective Communication", "Proposal Writing", "Product Design", "Leadership", "Teamwork", "Creative Problem Solving"],
        "goal_description": "To create a comprehensive business proposal for 'Repair Me,' an on-the-go repair service, detailing the business model, market size, customer journey, and additional features.",
        "how_it_works": {
            "Current Process Analysis": "Analyze the current repair process and identify pain points for both consumers and vendors.",
            "Solution Proposition": "Propose 'Repair Me,' a service that allows users to book repair services with a single click, providing additional features such as warranties, on-the-go repairs, and customer protection.",
            "Market Analysis": "Evaluate the market size and potential reach, focusing on smartphone users in the JABODETABEK area.",
            "Business Model": "Outline the business model, including transaction share, premium memberships, and sale profit.",
            "Vendor Validation": "Validate the business model with potential vendors, analyzing customer flow, idle time, and profit margins."
        },
        "technical_skills": {
            "PowerPoint": "Creating detailed and persuasive presentations to communicate the business proposal effectively."
        },
        "advanced_skills": {
            "Business Analysis": "Expertise in analyzing the market and business environment to develop a robust business proposal.",
            "Presentation Design": "Designing a compelling presentation that clearly conveys the business idea and its benefits.",
            "Product Design": "Innovative approach to designing the Repair Me service, ensuring it meets user needs and enhances their experience."
        },
        "soft_skills": {
            "Attention to Detail": "Ensuring all aspects of the business proposal are meticulously crafted and accurate.",
            "Effective Communication": "Clearly conveying the business proposal and its benefits through well-structured presentations and discussions.",
            "Proposal Writing": "Crafting a detailed and persuasive business proposal that effectively communicates the project goals, methodologies, and anticipated impacts.",
            "Leadership": "Demonstrating strong leadership skills in managing teams, projects, and driving organizational success.",
            "Teamwork": "Collaborating effectively with team members to achieve common goals and deliver high-quality results.",
            "Creative Problem Solving": "Utilizing creative approaches to tackle repair service challenges and develop effective solutions."
        },
        "image": None,  # Path to the image file if available
        "video": None,  # Path to the video file if available
        "URL": "repair_me_proposal.pdf"
    },

    "Robo Warung Business Proposal": {
        "skills": ["PowerPoint", "Business Analysis", "Presentation Design", "Attention to Detail", "Effective Communication", "Proposal Writing", "Product Design", "Leadership", "Teamwork", "Creative Problem Solving"],
        "goal_description": "To create a comprehensive business proposal for 'Robo Warung,' a set of apps designed to help warungs manage their business and provide companies with insights into product performance.",
        "how_it_works": {
            "Market Analysis": "Evaluate the market size and potential reach, focusing on various types of stores including supermarkets, mini markets, hypermarkets, and traditional groceries.",
            "Solution Proposition": "Propose 'Robo Warung,' which includes a warung app for managing transactions, inventories, and generating reports; a customer app for online orders and subscriptions; and a company app for accessing sales performance and consumer research data.",
            "Business Model": "Outline the business model, including free and premium subscription options, profit sharing, and targeted promotions.",
            "Marketing Plan": "Detail the marketing plan, including user acquisition strategies, brand awareness campaigns, and customer retention methods."
        },
        "technical_skills": {
            "PowerPoint": "Creating detailed and persuasive presentations to communicate the business proposal effectively."
        },
        "advanced_skills": {
            "Business Analysis": "Expertise in analyzing the market and business environment to develop a robust business proposal.",
            "Presentation Design": "Designing a compelling presentation that clearly conveys the business idea and its benefits.",
            "Product Design": "Innovative approach to designing the Robo Warung apps, ensuring they meet user needs and enhance their experience."
        },
        "soft_skills": {
            "Attention to Detail": "Ensuring all aspects of the business proposal are meticulously crafted and accurate.",
            "Effective Communication": "Clearly conveying the business proposal and its benefits through well-structured presentations and discussions.",
            "Proposal Writing": "Crafting a detailed and persuasive business proposal that effectively communicates the project goals, methodologies, and anticipated impacts.",
            "Leadership": "Demonstrating strong leadership skills in managing teams, projects, and driving organizational success.",
            "Teamwork": "Collaborating effectively with team members to achieve common goals and deliver high-quality results.",
            "Creative Problem Solving": "Utilizing creative approaches to tackle warung management challenges and develop effective solutions."
        },
        "image": None,  # Path to the image file if available
        "video": None,  # Path to the video file if available
        "URL": "robo_warung_proposal.pdf"
    },

    "Modular Bag Business Proposal": {
        "skills": ["Microsoft Word", "Business Analysis", "Presentation Design", "Attention to Detail", "Effective Communication", "Proposal Writing", "Product Design", "Leadership", "Teamwork", "Creative Problem Solving"],
        "goal_description": "To create a comprehensive business proposal for 'Doradush Bag,' a modular and adjustable bag designed to cater to various user needs and preferences.",
        "how_it_works": {
            "Market Analysis": "Evaluate the market size and potential reach, focusing on different demographic segments including students, professionals, and photographers.",
            "Solution Proposition": "Propose 'Doradush Bag,' a versatile and modular bag that can be adjusted according to the user's needs, offering different modules for laptops, cameras, and daily essentials.",
            "Business Model": "Outline the business model, including pricing strategies, distribution channels, and marketing plans.",
            "Product Features": "Highlight the key features of Doradush Bag, such as customizable parts and straps, durability, and ergonomic design."
        },
        "technical_skills": {
            "PowerPoint": "Creating detailed and persuasive presentations to communicate the business proposal effectively."
        },
        "advanced_skills": {
            "Business Analysis": "Expertise in analyzing the market and business environment to develop a robust business proposal.",
            "Presentation Design": "Designing a compelling presentation that clearly conveys the business idea and its benefits.",
            "Product Design": "Innovative approach to designing the Doradush Bag, ensuring it meets user needs and enhances their experience."
        },
        "soft_skills": {
            "Attention to Detail": "Ensuring all aspects of the business proposal are meticulously crafted and accurate.",
            "Effective Communication": "Clearly conveying the business proposal and its benefits through well-structured presentations and discussions.",
            "Proposal Writing": "Crafting a detailed and persuasive business proposal that effectively communicates the project goals, methodologies, and anticipated impacts.",
            "Leadership": "Demonstrating strong leadership skills in managing teams, projects, and driving organizational success.",
            "Teamwork": "Collaborating effectively with team members to achieve common goals and deliver high-quality results.",
            "Creative Problem Solving": "Utilizing creative approaches to tackle bag design challenges and develop effective solutions."
        },
        "image": None,  # Path to the image file if available
        "video": None,  # Path to the video file if available
        "URL": "doradush_bag_proposal.pdf"
    },
## #####################################################################################3#######################################################################3 STREAMLIT
    "Restoran Review WebApp": {
        "skills": ["Python Programming", "Firestore Database", "Google Storage API", "Basic HTML and CSS", "Web Creation", "Attention to Detail", "Effective Communication","Database Management"],
        "goal_description": "To create a user-friendly platform where customers can submit reviews and ratings for 'Restoran Ramesin,' and view other users' reviews.",
        "how_it_works": {
            "User Submission Form": "Users can submit their reviews through a form that includes fields for order ID, review text, reviewer's name, rating, and an image of their meal.",
            "Image Upload to GCS": "The image is uploaded to Google Cloud Storage, and a signed URL is generated for access.",
            "Storing Reviews in Firestore": "The review text, image URL, reviewer’s name, and rating are stored in Google Firestore along with a timestamp.",
            "Fetching and Displaying Reviews": "Reviews are fetched from Firestore and displayed in a visually appealing format, including the review text, reviewer's name, rating, and meal image."
        },
        "technical_skills": {
            "Python Programming": "The main programming language used for developing the application.",
            "Firestore Database": "Utilizing Firestore for real-time database management and seamless data synchronization.",
            "Google Storage API": "Using Google Storage API for efficient storage and retrieval of meal images.",
            "Basic HTML and CSS": "Enhancing the web interface using HTML and CSS.",

        },
        "advanced_skills": {
            "Database Management": "Ensures data integrity, security, and optimal performance, critical for maintaining accurate and reliable project management data.",
            "Basic Website Creation": "Developing intuitive and visually appealing web interfaces for the application."
        },
        "soft_skills": {
            "Attention to Detail": "Ensuring meticulous accuracy and thoroughness in all tasks, significantly reducing the potential for errors.",
        },
        "image": None,  # Path to the image file if available
        "video": "restoran_review.mp4",  # Path to the video file if available
        "URL": None
    },

    "Project Management Dashboard": {
        "skills": ["Python Programming", "MySQL", "Google Cloud", "Basic HTML and CSS for Streamlit", "Attention to Detail", "Effective Communication",  "Database Management","Basic Website Creation"],
        "goal_description": "To develop a comprehensive project management dashboard for managing users, projects, and tasks efficiently.",
        "how_it_works": {
            "User Registration": "Users can register with a username and password, which are securely stored in the database using bcrypt for hashing.",
            "User Login": "Registered users can log in to the system using their credentials, with validation against the hashed passwords stored in the database.",
            "Project and Task Management": "Users can create, update, and delete projects and tasks. Only one project can be active at a time, and tasks can be marked as complete or incomplete.",
            "Data Storage": "All user, project, and task data is stored in MySQL, ensuring data integrity and security.",
            "User Status Management": "Users can pause and resume their projects, and the system automatically deducts days remaining for active users."
        },
        "technical_skills": {
            "Python Programming": "The main programming language used for developing the application.",
            "MySQL": "Utilizing MySQL for managing and querying relational databases.",
            "Google Cloud": "Leveraging Google Cloud services for scalable and secure cloud computing solutions.",
            "Basic HTML and CSS for Streamlit": "Enhancing the appearance and functionality of the Streamlit application using HTML and CSS."
        },
        "advanced_skills": {
            "Database Management": "Ensures data integrity, security, and optimal performance, critical for maintaining accurate and reliable project management data.",
            "Basic Website Creation": "Developing intuitive and visually appealing web interfaces for the application, enhancing user experience and interaction."
        },
        "soft_skills": {
            "Attention to Detail": "Ensuring meticulous accuracy and thoroughness in all tasks, significantly reducing the potential for errors.",
            "Effective Communication": "Clearly conveying project statuses and updates through well-structured dashboards and notifications."
        },
        "image": None,  # Path to the image file if available
        "video": "project_management_dashboard.mp4",  # Path to the video file if available
        "URL": None
    },
}


api_key = st.secrets["AIRTABLE_TOKEN"]
base_id = st.secrets["AIRTABLE_BASE_ID"]
table_name = "Form"  # Airtable table name

# Initialize Airtable
api = Api(api_key)
table = api.table(base_id, table_name)



technical_skills_description = "Tools and technologies used to implement the project."
advanced_skills_description = "Combining multiple tools and techniques to achieve complex tasks."
soft_skills_description = "Personal attributes that enable effective collaboration and task execution."
showcase= " Image and video that proof of development or the result of the app"


st.set_page_config(page_title='My Portfolio', layout='wide', page_icon=':tada:')

# Function to set the state and rerun the app
def set_state(page=None, selected_project=None):
    st.query_params.clear()  # Clear all query parameters
    st.session_state.clear()  # Reset the session state

    if page:
        st.session_state['page'] = page

    if selected_project:
        st.session_state['selected_project'] = selected_project

    # Update query parameters (using st.query_params)
    params = st.query_params.to_dict()  # Get all parameters as a dictionary
    if 'page' in st.session_state:
        params['page'] = st.session_state['page']
    if 'selected_project' in st.session_state:
        params['selected_project'] = st.session_state['selected_project']

    if 'selected_skill' in params:
        del params['selected_skill']

    st.query_params.update(params)
    time.sleep(0.1)
    st.rerun()



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        

def show_pdf(file_path):
    with open(file_path, "rb") as f:
        pdf_viewer(f.read(), width=700, height=500)

def set_state_project(page=None, selected_skill=None):
    st.session_state.clear()  # Reset the session state
    if page in ['resume', 'contact', 'request', 'home']:
        st.session_state['selected_skill'] = None
    if page:
        st.session_state['page'] = page
    if selected_skill is not None:
        st.session_state['selected_skill'] = selected_skill

    # Update query parameters (using st.query_params)
    params = st.query_params.to_dict()  # Get all parameters as a dictionary
    if 'page' in st.session_state:
        params['page'] = st.session_state['page']
    if 'selected_skill' in st.session_state and st.session_state['selected_skill'] is not None:
        params['selected_skill'] = st.session_state['selected_skill']

    st.query_params.update(params)
    time.sleep(0.1)
    st.rerun()
    
# Check if session_state keys exist, if not, initialize them
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'  # Default to 'home'
if 'selected_skill' not in st.session_state:
    st.session_state['selected_skill'] = None

if 'selected_project' not in st.session_state:
    st.session_state['selected_project'] = None

# Check query parameters (using st.query_params)
query_params = st.query_params
if 'page' in query_params:
    st.session_state['page'] = query_params['page']
if 'selected_skill' in query_params:
    st.session_state['selected_skill'] = query_params['selected_skill']
# Load your photo
photo = Image.open("photo.png")  # Replace with your photo file path

# Your details
name = "Welcome to Hanif portfolio"
profile_description = """
I am a versatile technology professional with a deep understanding of business processes,
dedicated to accelerating operations and driving efficiency through innovative solutions.
"""

def redirect(url):
    st.markdown(f'<meta http-equiv="refresh" content="0; url={url}" />', unsafe_allow_html=True)


with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def render_home():
    # Main content
    st.markdown(f"<h1>Hi, welcome to Hanif portfolio</h1>", unsafe_allow_html=True)

    # Display photo centered
    col1, col2, col3 = st.columns([3, 1, 3])
    
    with col2:
        st.image(photo, width=300)

    # Description
    st.markdown(f"<p class='profile_description'>Click the skill to see the projects I do with that skill.</p>", unsafe_allow_html=True)
    
    # Buttons
    st.markdown("<hr>", unsafe_allow_html=True)
    col1, col2, col3,col4 = st.columns(4)
    with col1:
        if st.button("See Resume"):
            set_state(page='resume')
    with col2:
        if st.button("See All Projects"):
            set_state(page='projects')
    with col3:
        if st.button("Connect with me!"):
            set_state(page='contact')
    with col4:
        st.link_button("Chat With My Bot!", url="https://chatgpt.com/g/g-3HRu9clyI-hanif-r-gpt")

    st.markdown("<hr>", unsafe_allow_html=True)

    # Technical Skills Section
    st.markdown(f"<h2 title='{technical_skills_description}'>Technical Skills</h2>", unsafe_allow_html=True)
    tech_skill_columns = st.columns(3)
    for i, (skill, skill_description) in enumerate(technical_skills.items()):
        col = tech_skill_columns[i % 3]
        with col:
            if st.button(skill):
                set_state_project(page='skills', selected_skill=skill)

    # Advanced Skills Section
    st.markdown(f"<h2 title='{advanced_skills_description}'>Advanced Skills</h2>", unsafe_allow_html=True)
    advanced_skill_columns = st.columns(3)
    for i, (skill, skill_description) in enumerate(advanced_skills.items()):
        col = advanced_skill_columns[i % 3]
        with col:
            if st.button(skill):
                set_state_project(page='skills', selected_skill=skill)
                
    # Soft Skills Section
    st.markdown(f"<h2 title='{soft_skills_description}'>Soft Skills</h2>", unsafe_allow_html=True)
    soft_skill_columns = st.columns(3)
    for i, (skill, skill_description) in enumerate(soft_skills.items()):
        col = soft_skill_columns[i % 3]
        with col:
            if st.button(skill):
                set_state_project(page='skills', selected_skill=skill)


def render_resume():
    # Construct the absolute path to the file
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'Document', 'resume.pdf')

    try:
        with open(file_path, "rb") as f:
            pdf_data = f.read()

            # Use the streamlit-pdf-viewer component to display the PDF
            pdf_viewer(pdf_data, width=700, height=500)
            
            # Provide a download button
            st.download_button(
                label="Download Resume",
                data=pdf_data,
                file_name="resume.pdf",
                mime="application/pdf"
            )
            
    except FileNotFoundError as e:
        st.error(f"Error: {e}")
        st.write("Resume file not found.")
        
    if st.button("Back to Home"):
        set_state(page='home')

def render_skill():
    st.markdown("<h1>Projects with selected skill</h1>", unsafe_allow_html=True)
    if st.session_state['selected_skill']:
        skill = st.session_state['selected_skill']
        st.markdown(f"<h2>Projects with {skill}</h2>", unsafe_allow_html=True)
        if skill in technical_skills:
            st.write(f"**Skill Description**: {technical_skills[skill]}")
        else:
            st.write(f"**Skill Description**: {soft_skills[skill]}")
        filtered_projects = {project: proj_data for project, proj_data in projects.items() if skill in proj_data['skills']}
    else:
        filtered_projects = projects

    for project, proj_data in filtered_projects.items():
        with st.expander(project):
            st.write(f"**Skills Demonstrated**: {', '.join(proj_data['skills'])}")
            
            st.write(f"### Goal and Description")
            st.write(proj_data['goal_description'])
            
            st.write(f"### How It Works")
            for step, description in proj_data['how_it_works'].items():
                st.write(f"**{step}**: {description}")

            st.markdown(f"<h2 title='{technical_skills_description}'>Technical Skills</h2>", unsafe_allow_html=True)
            for skill, description in proj_data['technical_skills'].items():
                st.write(f"**{skill}**: {description}")

            st.markdown(f"<h2 title='{advanced_skills_description}'>Advanced Skills</h2>", unsafe_allow_html=True)
            for skill, description in proj_data['advanced_skills'].items():
                st.write(f"**{skill}**: {description}")

            st.markdown(f"<h2 title='{soft_skills_description}'>Soft Skills</h2>", unsafe_allow_html=True)
            if proj_data['soft_skills'] != "None":
                for skill, description in proj_data['soft_skills'].items():
                    st.write(f"**{skill}**: {description}")
            st.markdown(f"<h2 title='{showcase}'>Image and Video</h2>", unsafe_allow_html=True)
            if proj_data.get("image"):
                image_path = os.path.join(os.path.dirname(__file__), 'Pictures', proj_data["image"])
                st.image(image_path)
            if proj_data.get("video"):
                video_path = os.path.join(os.path.dirname(__file__), 'Video', proj_data["video"])
                st.video(video_path)
            if proj_data.get("URL"):
                pdf_path = os.path.join(os.path.dirname(__file__), 'Document', proj_data["URL"])
                show_pdf(pdf_path)
    
    if st.button("Back to Home"):
        set_state(page='home')

def render_projects():
    st.markdown("<h1>Projects</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    for i, project in enumerate(projects):
        col = [col1, col2, col3][i % 3]
        with col:
            if st.button(project):
                st.session_state.selected_project = project

    if 'selected_project' in st.session_state:
        selected_project = st.session_state['selected_project']
        if selected_project in projects:
            
            with st.expander(selected_project, expanded=True):
                proj_data = projects[selected_project]
                st.write(f"**Skills Demonstrated**: {', '.join(proj_data['skills'])}")
                st.write(f"### Goal and Description")
                st.write(proj_data['goal_description'])
                st.write(f"### How It Works")
                for step, description in proj_data['how_it_works'].items():
                    st.write(f"**{step}**: {description}")

                st.markdown(f"<h2>Technical Skills</h2>", unsafe_allow_html=True)
                for skill, description in proj_data['technical_skills'].items():
                    st.write(f"**{skill}**: {description}")

                st.markdown(f"<h2>Advanced Skills</h2>", unsafe_allow_html=True)
                for skill, description in proj_data['advanced_skills'].items():
                    st.write(f"**{skill}**: {description}")

                st.markdown(f"<h2>Soft Skills</h2>", unsafe_allow_html=True)
                if proj_data['soft_skills'] != "None":
                    for skill, description in proj_data['soft_skills'].items():
                        st.write(f"**{skill}**: {description}")

                st.markdown(f"<h2>Image and Video</h2>", unsafe_allow_html=True)
                if proj_data.get("image"):
                    image_path = os.path.join(os.path.dirname(__file__), 'Pictures', proj_data["image"])
                    st.image(image_path)
                if proj_data.get("video"):
                    video_path = os.path.join(os.path.dirname(__file__), 'Video', proj_data["video"])
                    st.video(video_path)
                if proj_data.get("URL"):
                    pdf_path = os.path.join(os.path.dirname(__file__), 'Document', proj_data["URL"])
                    show_pdf(pdf_path)

    if st.button("Back to Home"):
        set_state(page='home')
        
def render_contact():

    local_css("style.css")

    # ------------------------------------------------------------
    #
    #                        front-end
    #
    # ------------------------------------------------------------

    f = open("cards.txt")

    st.markdown(str(f.read()), unsafe_allow_html=True)

    f.close()

    if st.button("Back to Home"):
        set_state(page='home')

def render_request():
    st.title("Request Form")

    with st.form(key='request_form'):
        st.subheader("Submit Your Request")
        code_input = st.text_input("Enter your request code", "")
        request_details = st.text_area("Request Details", "")
        submit_button = st.form_submit_button("Submit Request")

    if submit_button:
        if code_input and request_details:
            # Fetch code from Airtable with retries
            records = fetch_records_with_retries(table, formula=f"{{Code}} = '{code_input}'")
            if records:
                record = records[0]
                usage_number = record['fields'].get('Usage Number', 0)
                if usage_number > 0:
                    # Update the record with decremented usage number and new request details
                    new_usage_number = usage_number - 1
                    table.update(record['id'], {
                        'Usage Number': new_usage_number,
                        'Request Details': request_details,
                        'Status': 'Pending'
                    })
                    st.session_state.page = 'success'
                    st.rerun()
                else:
                    st.error("Insufficient usage number for this code.")
            else:
                st.error("Invalid code or unable to fetch records.")
        else:
            st.error("Please fill all fields before submitting.")

    if st.button("Don't have a code? Click here"):
        set_state(page='request_code')

 
    if st.button("Back to Home"):
        set_state(page='home')







def show_contact_form():
    with st.form(key='contact_form'):
        st.subheader("Contact Form")
        name = st.text_input("Name", "")
        company_name = st.text_input("Company", "")
        contact_method = st.text_input("Contact (Email/Phone)", "")
        request_type = st.selectbox("Type", ["Hiring / Commision", "Challenge", "Feedback","Question"])
        additional_request = st.text_area("Request Details", "")
        submit_contact = st.form_submit_button("Submit Contact Request")

    if submit_contact:
        if name and company_name and contact_method and request_type and additional_request:
            try:
                # Add a contact request to Airtable
                table.create({
                    'Full Name': name,
                    'Company': company_name,
                    'Contact Info': contact_method,
                    'Type': request_type,
                    'Request Details': additional_request,
                    'Status': 'Pending'
                })
                st.session_state.page = 'success'
                st.rerun()
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error("Please fill all fields before submitting.")

    if st.button("Back to Home"):
        set_state(page='home')

def show_success_page():
    st.success("Your request has been submitted successfully!")
    st.write("Contact this number xxxxx or this email xx for further information.")
    if st.button("Submit another request"):
        set_state(page='request')

    if st.button("Back to Home"):
        set_state(page='home')


def fetch_records_with_retries(table, formula, retries=3, delay=5):
    """Fetch records from Airtable with retries."""
    for attempt in range(retries):
        try:
            return table.all(formula=formula)
        except HTTPError as e:
            st.error(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    st.error("Failed to fetch records after several attempts.")
    return []
# Render the selected page
if st.session_state['page'] == 'home':
    render_home()
elif st.session_state['page'] == 'resume':
    render_resume()
elif st.session_state['page'] == 'projects':
    render_projects()
elif st.session_state['page'] == 'contact':
    render_contact()
elif st.session_state['page'] == 'request':
    render_request()

elif st.session_state['page'] == 'skills':
    render_skill()
elif st.session_state['page'] == 'request_code':
    show_contact_form()

elif st.session_state['page']  == 'success':
    show_success_page()
