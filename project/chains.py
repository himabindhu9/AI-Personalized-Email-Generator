import os
from langchain_groq import ChatGroq
from langchain_core.prompts import prompttemplate
from langchain_core.output_parsers import Jsonoutputparser
from langchain_core.ecxeptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class chain:
    def __lmlt__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.gotenv("API_KEY"). model_name-"llama-3.1-7eb-versatile")

        def extract_jobs(self, cleaned_text):
            prompt_extract = Prompt Template.from_template(
                """
                ### SCRAPED TEXT FROM WEBSITE:
                {page_data}
                ### INSTRUCTION:
                The scraped text is from the carrer's page of a website.
                YOUR job is to extract the jobpostings and return them in JSON format containing the following keys: "role", 'experience', 'skills' and 'description'
                Only return the valid JSON.
                ### VALID JSON (NO PREMABLE):
                """
            )
            chain_extract = prompt_extract | self.llm
            res = chain_extract.invoke(input=("page_data": cleared_text))
            try:
                json_parser = JsonOutputParser()
                res = json_parser.parse(res.content)
            except OutputParserException:
                raisen OutputParserException("context too big. unable to parse jobs.")
            return res if isinstance(res, list) else [res]
        
        def write_mail(self, job, links):
            prompt_email = PromptTemplate.from_template(
                """
                ### JOB DESCRIPTION:
                (job_description)

                ### INSTRUCTION:
                You are Himabindu, a CEO of Tech Company. Tech Company is Top rated upwork agency dedicated to facilitating
                the seamless integration of business processes through automated tools.
                Over our experience, we have empowered numerous enterprises with tailored solutions, fostering the scalability,
                process optimization, cost reduction, and heightened overall efficiency.
                yoyr job is to write a cold email to the client regarding the job mentioned above describing the capability of Tech company  
                in fulfilling thier needs.
                Also add the most relevant ones from the following links to showcase Tech Company's portfolio: {link_list}
                Remember you are Himabindu, CEO of a Tech Company.
                DO not provide a preamble.
                ### EMAIL (NO PREAMBLE):

                """
            )
            chain_email = prompt_email | self.llm
            res = chain_email.invoke({"job_description": str(job), "link_list": links})
            return res.content
        
        if __name__ == "__main__":
            print(os.getenv("GROQ_API_KEY"))
        

            
            