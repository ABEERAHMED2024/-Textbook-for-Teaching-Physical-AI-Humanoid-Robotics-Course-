import React, { useState, useEffect, useRef } from 'react';


// Define the type for glossary entries
interface GlossaryEntry {
  id: string;
  term: string;
  definition: string;
  relatedTerms?: string[];
  chapters?: string[];
}

// Define the props interface
interface GlossarySearchProps {
  glossaryData: GlossaryEntry[]; // Pass glossary data as prop
}

const GlossarySearch: React.FC<GlossarySearchProps> = ({ glossaryData }): JSX.Element => {
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState<GlossaryEntry[]>([]);
  const [isSearching, setIsSearching] = useState(false);
  const searchIndex = useRef<any>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  // Initialize the search index when component mounts
  useEffect(() => {
    // Dynamically import FlexSearch to handle both client and server environments
    const initializeSearch = async () => {
      const FlexSearch = await import('flexsearch');

      // Create a new FlexSearch index
      searchIndex.current = new FlexSearch.Index({
        tokenize: "forward",
        resolution: 9,
      });

      // Add glossary entries to the index
      glossaryData.forEach(entry => {
        const content = `${entry.term} ${entry.definition} ${entry.relatedTerms?.join(' ') || ''}`;
        searchIndex.current.add(entry.id, content);
      });
    };

    initializeSearch();
  }, [glossaryData]);

  // Perform search when query changes
  useEffect(() => {
    if (!searchIndex.current || searchQuery.trim() === '') {
      setSearchResults([]);
      return;
    }

    setIsSearching(true);

    // Simulate async search for better UX
    const timer = setTimeout(() => {
      const resultIds = searchIndex.current.search(searchQuery, 10); // Limit to 10 results

      // Map the result IDs back to glossary entries
      const foundEntries = resultIds
        .map((id: string) => glossaryData.find(entry => entry.id === id))
        .filter(Boolean) as GlossaryEntry[];

      setSearchResults(foundEntries);
      setIsSearching(false);
    }, 150); // Debounce search by 150ms

    return () => clearTimeout(timer);
  }, [searchQuery, glossaryData]);

  return (
    <div className="glossary-search">
      <div className="search-container">
        <input
          ref={inputRef}
          type="text"
          placeholder="Search glossary terms..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="search-input"
        />
        {searchQuery && (
          <button
            onClick={() => {
              setSearchQuery('');
              inputRef.current?.focus();
            }}
            className="clear-button"
            aria-label="Clear search"
          >
            ×
          </button>
        )}
      </div>

      {isSearching && <div className="searching">Searching...</div>}

      {searchResults.length > 0 && (
        <div className="search-results">
          <h3>Search Results</h3>
          <ul>
            {searchResults.map((entry) => (
              <li key={entry.id} className="result-item">
                <h4>{entry.term}</h4>
                <p>{entry.definition}</p>
                {entry.relatedTerms && entry.relatedTerms.length > 0 && (
                  <div className="related-terms">
                    <strong>Related terms:</strong> {entry.relatedTerms.join(', ')}
                  </div>
                )}
                {entry.chapters && entry.chapters.length > 0 && (
                  <div className="related-chapters">
                    <strong>Used in:</strong> {entry.chapters.join(', ')}
                  </div>
                )}
              </li>
            ))}
          </ul>
        </div>
      )}

      {searchQuery && searchResults.length === 0 && !isSearching && (
        <div className="no-results">
          No terms found matching "{searchQuery}"
        </div>
      )}
    </div>
  );
};

export default GlossarySearch;