import React, { useState, useEffect } from 'react';
import FlexSearch from 'flexsearch';
import glossaryData from '@site/static/data/glossary-index.json';

import styles from './GlossarySearch.module.css';

interface GlossaryEntry {
  id: number;
  term: string;
  definition: string;
  acronym?: string;
  relatedTerms?: string[];
  chapters?: string[];
}

const GlossarySearch: React.FC = () => {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<GlossaryEntry[]>([]);
  const [index, setIndex] = useState<any>(null);

  useEffect(() => {
    // Initialize FlexSearch index
    const searchIndex = new FlexSearch.Document({
      id: 'id',
      index: [
        { field: 'term', tokenize: 'forward' },
        { field: 'definition', tokenize: 'forward' },
        { field: 'acronym', tokenize: 'forward' },
        { field: 'relatedTerms', tokenize: 'forward' }
      ]
    });

    // Add glossary entries to index
    glossaryData.terms.forEach((entry: GlossaryEntry) => {
      searchIndex.add(entry.id, {
        id: entry.id,
        term: entry.term,
        definition: entry.definition,
        acronym: entry.acronym || '',
        relatedTerms: entry.relatedTerms?.join(' ') || ''
      });
    });

    setIndex(searchIndex);
  }, []);

  useEffect(() => {
    if (!index || !query) {
      setResults([]);
      return;
    }

    // Perform search across all indexed fields
    const searchResults = index.search(query, {
      index: ['term', 'definition', 'acronym', 'relatedTerms'],
      limit: 10,
      enrich: true
    });

    // Extract the actual documents from search results
    const documents = searchResults.flatMap((result: any) => result.result);
    const foundEntries = documents
      .map((id: number) => glossaryData.terms.find((entry: GlossaryEntry) => entry.id === id))
      .filter(Boolean) as GlossaryEntry[];

    setResults(foundEntries);
  }, [query, index]);

  return (
    <div className={styles.glossarySearch}>
      <div className={styles.searchContainer}>
        <input
          type="text"
          placeholder="Search glossary terms..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className={styles.searchInput}
        />
        {query && (
          <button 
            onClick={() => setQuery('')}
            className={styles.clearButton}
            aria-label="Clear search"
          >
            ✕
          </button>
        )}
      </div>
      
      {results.length > 0 && (
        <div className={styles.resultsContainer}>
          <h3 className={styles.resultsTitle}>Glossary Results</h3>
          <ul className={styles.resultsList}>
            {results.map((entry) => (
              <li key={entry.id} className={styles.resultItem}>
                <div className={styles.termContainer}>
                  <h4 className={styles.term}>
                    {entry.term}
                    {entry.acronym && <span className={styles.acronym}>({entry.acronym})</span>}
                  </h4>
                </div>
                <p className={styles.definition}>{entry.definition}</p>
                {entry.relatedTerms && entry.relatedTerms.length > 0 && (
                  <div className={styles.relatedTerms}>
                    <strong>Related:</strong> {entry.relatedTerms.join(', ')}
                  </div>
                )}
                {entry.chapters && entry.chapters.length > 0 && (
                  <div className={styles.chapters}>
                    <strong>Used in:</strong> {entry.chapters.join(', ')}
                  </div>
                )}
              </li>
            ))}
          </ul>
        </div>
      )}
      
      {query && results.length === 0 && (
        <div className={styles.noResults}>
          No glossary terms found for "{query}"
        </div>
      )}
    </div>
  );
};

export default GlossarySearch;