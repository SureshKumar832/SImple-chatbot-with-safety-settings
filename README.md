# ⭐ Streamlit + Google Gemini Chatbot

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-%3E%3D1.20.0-orange.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)
[![Status](https://img.shields.io/badge/status-Prototype-yellowgreen.svg)]

> A lightweight Streamlit chatbot powered by Google Gemini with safety filters and typewriter-style responses.

---

## 🔖 Project Overview

TruthLens is an interactive chatbot web app built with **Streamlit** and Google **Gemini (Generative AI)**. It includes configurable safety settings, a typewriter-style response animation, and chat-history persistence in `st.session_state`.

---

## 🚀 Features

- Real-time chat using Google Gemini via `langchain_google_genai`
- Typewriter-style streaming responses for better UX
- Chat history stored in `st.session_state`
- Configurable safety settings (harassment, hate speech, sexual/dangerous content)
- Environment-based API key management (`.env`)

