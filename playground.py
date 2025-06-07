# Este seria o código CORRETO para a filosofia da Agnos
import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

# Carrega as variáveis de ambiente
load_dotenv()

def create_financial_analyst():
    try:
        # Criando um único agente com TODAS as ferramentas
        return Agent(
            name="Super Financial Analyst",
            role="Você é um assistente financeiro completo. Sua função é buscar informações na web e analisar dados de ações para responder às perguntas do usuário de forma abrangente.",
            # Usando o modelo correto da Groq
            model=Groq(id="llama3-70b-8192"), 
            
            # Dê ao agente todas as ferramentas disponíveis
            tools=[
                DuckDuckGoTools(),
                YFinanceTools(
                    stock_price=True,
                    analyst_recommendations=True,
                    stock_fundamentals=True,
                    company_news=True
                )
            ],
            instructions=[
                "Sempre use a ferramenta de busca para notícias recentes.",
                "Use as ferramentas financeiras para dados de mercado e recomendações.",
                "Combine todas as informações em uma resposta coesa e use tabelas para dados numéricos.",
                "Sempre inclua as fontes das notícias."
            ],
            show_tool_calls=True,
            markdown=True
        )
    except Exception as e:
        print(f"Erro ao criar o agente: {str(e)}")
        raise

def main():
    try:
        # Criar o agente
        analyst = create_financial_analyst()
        
        # Executar a análise
        analyst.print_response(
            "quais são as melhores ações para investir no momento com menor risco, Responda em português do Brasil.",
            stream=True
        )
    except Exception as e:
        print(f"Erro durante a execução: {str(e)}")

if __name__ == "__main__":
    main()