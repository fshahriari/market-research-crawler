import requests
from bs4 import BeautifulSoup
import json
from duckduckgo_search import DDGS

def get_website_data(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        title = soup.title.string.strip() if soup.title else "No Title"
        # استخراج متن‌های پاراگراف
        text = ' '.join([p.get_text() for p in soup.find_all('p')][:5])
        summary = text[:300] + "..." if len(text) > 300 else text
        
        return {"title": title, "summary": summary}
    except Exception as e:
        print(f"Error crawling {url}: {e}")
        return None

def main():
    print("--- Market Research Tool (DuckDuckGo Mode) ---")
    user_input = input("Enter a URL or search topic: ").strip()
    
    results = {}
    urls_to_process = []

    if user_input.startswith("http"):
        urls_to_process = [user_input]
    else:
        print(f"Searching for '{user_input}'...")
        # استفاده از موتور جستجوی DuckDuckGo
        with DDGS() as ddgs:
            results_ddg = list(ddgs.text(user_input, max_results=3))
            urls_to_process = [r['href'] for r in results_ddg]

    if not urls_to_process:
        print("No results found. Try a different query.")
        return

    for url in urls_to_process:
        print(f"Crawling: {url}")
        data = get_website_data(url)
        if data:
            results[url] = data
    
    with open('results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
        
    print(f"\nDone! Processed {len(results)} sites. Check 'results.json'.")

if __name__ == "__main__":
    main()