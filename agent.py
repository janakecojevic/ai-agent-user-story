from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)

def analiziraj_user_story(user_story):
    print("\n" + "="*50)
    print("AI AGENT - ANALIZA USER STORY")
    print("="*50)
    print(f"\nUlazna user story:\n{user_story}\n")

    print("KORAK 1: Analiza INVEST kriterijuma...")
    invest_rezultat = llm.invoke(f"""
    Analiziraj sledecu user story po INVEST kriterijumima:
    Independent, Negotiable, Valuable, Estimable, Small, Testable
    User story: {user_story}
    Za svaki kriterijum daj ocenu 1-5 i kratko objasnjenje.
    """)

    print("KORAK 2: Procena rizika...")
    rizik_rezultat = llm.invoke(f"""
    Analiziraj sledecu user story i identifikuj potencijalne rizike:
    User story: {user_story}
    Navedi rizike i preporuke.
    """)

    print("KORAK 3: Generisanje test case-ova...")
    test_rezultat = llm.invoke(f"""
    Na osnovu sledece user story generisi test case-ove:
    User story: {user_story}
    Navedi naziv, korake i ocekivani rezultat za svaki test.
    """)

    print("\n" + "="*50)
    print("REZULTATI:")
    print("="*50)
    print("\nINVEST ANALIZA:")
    print(invest_rezultat.content)
    print("\nRIZICI:")
    print(rizik_rezultat.content)
    print("\nTEST CASE-OVI:")
    print(test_rezultat.content)

user_story = """
Kao korisnik, zelim da mogu da resetujem lozinku putem email adrese,
kako bih mogao da pristupim nalogu ako zaboravim lozinku.
"""

analiziraj_user_story(user_story)
