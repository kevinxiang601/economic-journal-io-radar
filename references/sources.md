# Source map and reconciliation rules

## Journal identifiers and official inventories

| Journal | ISSN used for registries | Official current issue | Official online-first inventory |
|---|---|---|---|
| AER | 0002-8282 | https://www.aeaweb.org/journals/aer/issues | https://www.aeaweb.org/journals/search-results?from=a |
| JPE | 0022-3808 | https://www.journals.uchicago.edu/toc/jpe/current | https://www.journals.uchicago.edu/toc/jpe/0/0 |
| QJE | 0033-5533 | https://academic.oup.com/qje/issue | https://academic.oup.com/qje/advance-articles |
| JET | 0022-0531 | https://www.sciencedirect.com/journal/journal-of-economic-theory/issues | https://www.sciencedirect.com/journal/journal-of-economic-theory/articles-in-press |
| IIO | 0167-7187 | https://www.sciencedirect.com/journal/international-journal-of-industrial-organization/issues | https://www.sciencedirect.com/journal/international-journal-of-industrial-organization/articles-in-press |
| RAND J | 0741-6261 | https://onlinelibrary.wiley.com/journal/17562171 | https://onlinelibrary.wiley.com/toc/17562171/0/0 |
| Econometrica | 0012-9682 | https://onlinelibrary.wiley.com/journal/14680262 | https://www.econometricsociety.org/publications/econometrica |
| ReStud | 0034-6527 | https://academic.oup.com/restud/issue | https://academic.oup.com/restud/advance-articles |

Also query Crossref by ISSN on every run. Query OpenAlex when reachable and use IDEAS/RePEc or exact-title web search to reconcile remaining differences. A source counts as independent only if it is not a repost of the same search snippet.

## Reconciliation order

1. Take the union of Crossref, official current issue, and official online-first candidates.
2. Add candidates found only by OpenAlex/RePEc/exact-title search, then verify them at the DOI or publisher page.
3. Normalize DOI by lowercasing and removing `https://doi.org/`, `http://dx.doi.org/`, and `doi:`. Normalize titles by Unicode NFKD, removing punctuation, and collapsing whitespace.
4. For set differences, determine whether the record is a correction, front/back matter, issue information, delayed DOI deposit, or a genuine missing research article.
5. Record per-journal counts, checked channels and unresolved differences internally in existing task notes or working data. They support completeness and resumption, not a user-facing report appendix.

## Metadata authority

- DOI and title: publisher DOI page, then Crossref.
- Authors: publisher article page, then Crossref.
- First-online date: publisher page when shown; otherwise Crossref `published-online` or record creation date, explicitly labeled.
- Volume, issue, pages: publisher issue page, then Crossref.
- Abstract: publisher article page. A publisher-supplied Crossref abstract may support screening but is not a substitute for opening the article page.

Social posts, newsletters, institutional explainers, WeChat, and Xiaohongshu can reveal candidates or supply context. They never override bibliographic metadata or serve as the abstract source.

## Failure handling

- A blocked official page is not proof that the article is absent.
- When an official page is blocked, use DOI metadata plus one other structured source and say which official channel was inaccessible.
- When fewer than two channels are successfully checked for a journal, mark internal status `未完成交叉核验`; retain only a short local note in the digest if the limitation materially affects a retained claim.
- Do not call the run complete while an unexplained set difference remains.
