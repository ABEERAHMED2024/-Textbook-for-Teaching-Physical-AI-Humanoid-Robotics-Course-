/**
 * Personalization and Translation Service
 * 
 * Service to handle content personalization based on user background
 * and translation to Urdu
 */

import { BACKEND_URL } from '../constants';

class ContentService {
  /**
   * Personalize content based on user background
   * @param {string} content - The content to personalize
   * @returns {Promise<string>} - The personalized content
   */
  async personalizeContent(content) {
    try {
      const token = localStorage.getItem('access_token');
      
      if (!token) {
        throw new Error('User not authenticated');
      }

      const response = await fetch(`${BACKEND_URL}/api/personalization/personalize-content`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ content })
      });

      if (!response.ok) {
        throw new Error(`Failed to personalize content: ${response.statusText}`);
      }

      const data = await response.json();
      return data.personalized_content;
    } catch (error) {
      console.error('Error personalizing content:', error);
      throw error;
    }
  }

  /**
   * Get user background information
   * @returns {Promise<Object>} - User background information
   */
  async getUserBackground() {
    try {
      const token = localStorage.getItem('access_token');
      
      if (!token) {
        throw new Error('User not authenticated');
      }

      const response = await fetch(`${BACKEND_URL}/api/personalization/user-background`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });

      if (!response.ok) {
        throw new Error(`Failed to get user background: ${response.statusText}`);
      }

      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error getting user background:', error);
      throw error;
    }
  }

  /**
   * Translate content to Urdu
   * @param {string} content - The content to translate
   * @returns {Promise<string>} - The translated content
   */
  async translateToUrdu(content) {
    try {
      const token = localStorage.getItem('access_token');
      
      if (!token) {
        throw new Error('User not authenticated');
      }

      const response = await fetch(`${BACKEND_URL}/api/translation/translate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ 
          text: content,
          source_lang: 'en',
          target_lang: 'ur'
        })
      });

      if (!response.ok) {
        throw new Error(`Failed to translate content: ${response.statusText}`);
      }

      const data = await response.json();
      return data.translated_text;
    } catch (error) {
      console.error('Error translating content to Urdu:', error);
      throw error;
    }
  }
}

export default new ContentService();