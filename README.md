Reasoning Assistant Bot 🧠🤖
A modular multi-agent Reasoning Bot powered by Chain-of-Thought (CoT), ReAct, Toolformer, Camel agents — orchestrated with LangGraph.

🚀 Features
✅ Chain-of-Thought Agent (CoT)
→ Performs structured step-by-step reasoning.

✅ ReAct Agent
→ Combines reasoning with actions — uses tools if needed.

✅ Toolformer Agent
→ Decides when to use tools (calculator, PDF reader).

✅ Camel Agent
→ Provides answers from the perspective of different roles (Scientist, Lawyer, Artist, etc).

✅ LangGraph Flow
→ Orchestrates agents in a flexible, visualizable graph pipeline.

🗺️ Architecture
nginx
Copy code
Question → Chain-of-Thought → ReAct → Toolformer → Camel Agent → Answer
👉 State evolves step by step across agents.
👉 Each agent adds its result to shared state.

🛠️ Tools Integrated
✅ Calculator (real computation)

✅ PDF Reader (text extraction from PDF)

(More tools can be added easily)

⚙️ Stack
LangChain

LangGraph

Ollama (local LLMs)

Python 3.11+

📂 Project Structure
plaintext
Copy code
main.py                 # Entry point — runs agents and LangGraph flow
langgraph_flow.py       # LangGraph graph definition
cot_agent.py            # Chain-of-Thought agent
react_agent.py          # ReAct agent
toolformer_agent.py     # Toolformer agent
camel_agent.py          # Camel multi-role agent
tools/
    calculator.py       # Calculator tool
    pdf_reader.py       # PDF reader tool
🚀 How to Run
1️⃣ Clone repo
bash
Copy code
git clone https://github.com/your_username/reasoning-assistant.git
cd reasoning-assistant
2️⃣ Set up venv
bash
Copy code
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3️⃣ Run Reasoning Bot CLI
bash
Copy code
python main.py
✅ Example Output
plaintext
Copy code
=== Chain-of-Thought ===
Step 1: ...
Step 2: ...
Final Answer: ...

=== ReAct ===
Thought: ...
Action: ...
Observation: ...
Final Answer: ...

=== Toolformer ===
Decision: Use calculator
Observation: 75
Final Answer: 75

=== Camel Agent (Artist role) ===
Answer: ...

🤝 Credits
Built with ❤️ using:

LangChain

LangGraph

Ollama

Python

Inspired by advanced Reasoning Bot architectures


