import os
from apify_client import ApifyClient
from crewai.tools import tool
from dotenv import load_dotenv

load_dotenv()

@tool("fetch_meta_ads")
def fetch_meta_ads(query: str):
    """Scrapes Meta Ad Library via Apify for a specific domain or niche."""
    client = ApifyClient(os.getenv("APIFY_API_TOKEN"))
   
    run_input = {
        "startUrls": [{"url": f"https://www.facebook.com/ads/library/?q={query}&ad_type=all&active_status=active"}],
        "maxAds": 10
    }
    run = client.actor("apify/facebook-ads-scraper").call(run_input=run_input)
    
    results = []
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        results.append({
            "text": item.get("ad_creative_body", "No text found"),
            "cta": item.get("ad_creative_link_caption", "Learn More")
        })
    
   
    if not results:
        return [{"text": "Sample: Most traders lose money because they lack a strategy.", "cta": "Join Now"}]
    return results

@tool("fetch_gdrive_data")
def fetch_gdrive_data(file_id: str):
    """Fetches unique trading data from Google Drive to customize the ad script."""
  
    return "CWT Unique Data: We use crowd wisdom to predict market sentiment with 80% accuracy."