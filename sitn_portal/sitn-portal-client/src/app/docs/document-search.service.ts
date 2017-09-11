import { Injectable } from '@angular/core';
import { Http }       from '@angular/http';

import { Observable }     from 'rxjs/Observable';
import 'rxjs/add/operator/map';

import { Document }           from './document';

@Injectable()
export class DocumentSearchService {

  constructor(private http: Http) {}

  search(term: string): Observable<Document[]> {
    return this.http
               .get(`docs/docid=${term}`)
               .map(response => response.json().documents as Document[]);
  }
}
