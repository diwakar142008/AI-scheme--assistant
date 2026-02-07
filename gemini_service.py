from google import genai

# Use your API key locally
client = genai.Client(api_key="AIzaSyDv593yerxrel-8xKXnpnX2cNWUQwQQIX4")

def explain_scheme(scheme):
    return f"""
📌 **{scheme['name']}**

🎯 **Who is it for?**
This scheme is suitable for people in the *{scheme['category']}* category,
especially those belonging to *{scheme['social_category']}* communities.

💰 **Benefits**
{scheme['benefit']}

📄 **Documents Required**
{", ".join(scheme['documents'])}

⏰ **Last Date**
{scheme['last_date']}

🤖 *Explanation generated using Google Gemini Embeddings*
"""
