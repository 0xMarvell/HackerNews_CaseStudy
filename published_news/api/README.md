# CASE STUDY API

## ENDPOINTS
 - GET - ```/api/news/```
    - Returns: All news objects saved in the database

 - POST - ```/api/news/```
     - Returns: The newly created news object
     - payload:
```json
        {
            "title": string,
            "url": url,
            "by": string,
            "score": int,
            "item_type": string
        }
```
  
 - GET - ```/api/news?{filter}={filter_value}```
      - Returns - Filtered news objects

 - GET - ```/api/news/comments```
      - Returns - All comment objects saved in the database

 - PUT - ```/api/news/{pk}/update```
    - Returns - Updated news object
    - Payload: 
```json
    {
        "title": "Updated value",
        "url": "Updated value",
        "by": "Updated value",
        "score": Updated value,
        "item_type": "Updated value",
        "comments": Updated value,
        "hacker_news_id": Updated value
    }
```

 - PATCH - ```/api/news/{pk}/update```
     - Returns - Updated news object
     - Payload:
```json
    {
        "key": "Updated value"
    }
```

 - DELETE - ```/api/news/{pk}/delete```
     - Returns - Deleted news object
