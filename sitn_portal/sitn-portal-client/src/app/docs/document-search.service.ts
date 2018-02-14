import { Injectable } from '@angular/core';
import { Http }       from '@angular/http';

import { Observable }     from 'rxjs/Observable';
import 'rxjs/add/operator/map';

import { Document }           from './document';

declare var sitnDocsConst:object;

@Injectable()
export class DocumentSearchService {

  private documentsUrl = sitnDocsConst['documentsUrl'];

  constructor(private http: Http) {}

  search(term: string): Observable<Document[]> {
    return this.http
               .get(`${this.documentsUrl}/get/?docid=${term}`)
               .map(response => response.json().documents as Document[]);
  }
}
