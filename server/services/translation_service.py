"""
Translation Service Module

This module provides functionality to translate content to Urdu
without modifying source files. It uses an external translation API
to provide on-demand translation services.
"""

from typing import Optional
import requests
import os
import asyncio
import aiohttp
from functools import lru_cache


class TranslationService:
    """
    Service to translate content to Urdu without modifying source files.
    
    The service uses an external translation API to provide on-demand
    translation of content. Translations are cached to improve performance.
    """
    
    def __init__(self):
        # Use environment variable for translation API key
        self.api_key = os.getenv("TRANSLATION_API_KEY")
        self.base_url = os.getenv("TRANSLATION_API_BASE_URL", "https://api.mymemory.translated.net")
        # For caching translations
        self.translation_cache = {}
    
    @lru_cache(maxsize=1000)
    def translate_to_urdu_cached(self, text: str) -> str:
        """
        Translate text to Urdu with caching
        
        Args:
            text: Text to translate
            
        Returns:
            Translated text in Urdu
        """
        # This is a simplified implementation
        # In a real implementation, we would call an actual translation API
        return self._translate_to_urdu_api(text)
    
    async def translate_to_urdu_async(self, text: str) -> str:
        """
        Asynchronously translate text to Urdu
        
        Args:
            text: Text to translate
            
        Returns:
            Translated text in Urdu
        """
        # Check cache first
        if text in self.translation_cache:
            return self.translation_cache[text]
        
        # Perform translation
        translated = await self._translate_to_urdu_api_async(text)
        
        # Cache the result
        self.translation_cache[text] = translated
        
        return translated
    
    def _translate_to_urdu_api(self, text: str) -> str:
        """
        Translate text to Urdu using an external API
        
        Args:
            text: Text to translate
            
        Returns:
            Translated text in Urdu
        """
        # Fallback implementation if no API key is provided
        if not self.api_key:
            # Return a placeholder translation for demonstration
            return f"[URDU TRANSLATION PLACEHOLDER: {text[:50]}...]"
        
        try:
            # Example using MyMemory translation API
            url = f"{self.base_url}/get"
            params = {
                'q': text,
                'langpair': 'en|ur',
                'key': self.api_key
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            
            result = response.json()
            translated_text = result.get('responseData', {}).get('translatedText', text)
            
            return translated_text
        except Exception as e:
            print(f"Translation error: {e}")
            return f"[TRANSLATION ERROR: {text}]"
    
    async def _translate_to_urdu_api_async(self, text: str) -> str:
        """
        Asynchronously translate text to Urdu using an external API
        
        Args:
            text: Text to translate
            
        Returns:
            Translated text in Urdu
        """
        # Check if API key is available
        if not self.api_key:
            # Return a placeholder translation for demonstration
            return f"[URDU TRANSLATION PLACEHOLDER: {text[:50]}...]"
        
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.base_url}/get"
                params = {
                    'q': text,
                    'langpair': 'en|ur',
                    'key': self.api_key
                }
                
                async with session.get(url, params=params) as response:
                    response.raise_for_status()
                    
                    result = await response.json()
                    translated_text = result.get('responseData', {}).get('translatedText', text)
                    
                    return translated_text
        except Exception as e:
            print(f"Async translation error: {e}")
            return f"[TRANSLATION ERROR: {text}]"
    
    def translate_document(self, content: str, max_chunk_size: int = 500) -> str:
        """
        Translate a document to Urdu, handling large texts by splitting into chunks
        
        Args:
            content: Document content to translate
            max_chunk_size: Maximum size of text chunks to translate at once
            
        Returns:
            Translated document in Urdu
        """
        # Split content into paragraphs or sentences to avoid exceeding API limits
        paragraphs = content.split('\n\n')
        translated_paragraphs = []
        
        for paragraph in paragraphs:
            if len(paragraph) <= max_chunk_size:
                # Translate directly if small enough
                translated_paragraphs.append(self.translate_to_urdu_cached(paragraph))
            else:
                # Split into smaller chunks if too large
                sentences = paragraph.split('. ')
                current_chunk = ""
                
                for sentence in sentences:
                    if len(current_chunk + ". " + sentence) <= max_chunk_size:
                        current_chunk += ". " + sentence
                    else:
                        if current_chunk:
                            translated_paragraphs.append(self.translate_to_urdu_cached(current_chunk))
                        current_chunk = sentence
                
                # Translate remaining chunk
                if current_chunk:
                    translated_paragraphs.append(self.translate_to_urdu_cached(current_chunk))
        
        return '\n\n'.join(translated_paragraphs)