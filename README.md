
**Title:**  Resume Chatbot with Cohere & Next.js

**Description:**

A user-friendly chatbot application built with Next.js that leverages Cohere's powerful NLP capabilities to provide insightful and tailored answers to frequently asked resume-related questions.


**Project Overview:**

This project empowers users to gain valuable feedback on their resumes by engaging in an interactive chat with a Cohere-powered AI. The chatbot addresses common resume concerns, offering suggestions and guidance to enhance clarity, impact, and overall effectiveness.

**Features:**

* **Conversational Interface:** Users interact with the chatbot in a natural, question-and-answer format, making the experience intuitive and engaging.
* **RAG-powered Q&A**: Retrieval-Augmented Generation (RAG) improves the chatbot's accuracy by finding relevant passages from a pre-built knowledge base (e.g., resume best practices) before using Cohere's NLP to generate answers..
* **Cohere Integration:** Cohere's advanced NLP capabilities provide accurate and relevant information on resume-related topics.
* **Next.js Framework:** Leverages the benefits of Next.js for a performant and streamlined development experience.

**Technical Stack:**

* **Frontend:** Next.js
* **Backend:** Python (Flask)
* **Natural Language Processing (NLP):** Cohere

**Understanding RAG (R)**:

Retrieval-Augmented Generation (RAG) is a cutting-edge approach to question answering with large language models (LLMs) like Cohere. It combines two key steps:

Retrieval: The RAG system searches its knowledge base for relevant passages that align with the user's question. This knowledge base can be a collection of documents, FAQs, or other text resources related to resumes.
Augmented Generation: The LLM (Cohere in this case) analyzes the retrieved passages and uses them to inform its response. This helps to ensure that the chatbot's answers are grounded in factual information and targeted to the specific resume-related query.
This RAG approach enhances the accuracy and focus of the chatbot's responses compared to LLMs that generate answers solely based on their internal training data.

**Getting Started:**

**Prerequisites (R):**

* Node.js installed on your system. You can verify this by running `node -v` in your terminal.
* A Cohere account with API access. Refer to Cohere documentation for signup and API key retrieval instructions.
* Python installed on your system.

**Installation (A):**

1. Clone this repository:

   ```bash
   git clone https://github.com/nagaraj-real/nextjs-chat.git
   ```

2. Navigate to the project directory:

   ```bash
   cd nextjs-chat
   ```

3. Install dependencies:

   ```bash
   pnpm i
   ```

4. Add your Cohere API Key to .env

   ```bash
   COHERE_API_KEY= xxxxxxx
   ```

**Usage (G):**

1. Start the development server:

   ```bash
   pnpm dev
   ```

2. Access the chatbot in your web browser:

   - The default development server usually starts at `http://localhost:3000`. You might need to adjust the port number if it's already in use.


4. Update the file(test.pdf) to be used as context in app/api folder.
   You may need to update app.py as well with the new file details.

3. Type your resume-related questions into the chat interface. The chatbot will respond with helpful insights.


**Deployment (Optional):**

- If you intend to deploy the chatbot to a production environment, you'll need to follow specific instructions for your chosen hosting platform (e.g., Vercel, Netlify, AWS, etc.).
- Ensure proper environment variable configuration (e.g., Cohere API key) for your deployment.
