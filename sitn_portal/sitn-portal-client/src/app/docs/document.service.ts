import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';

import { Document } from './document';

declare var sitnDocsConst:object;

@Injectable()
export class DocumentService {
  getDocument(docid: string): Promise<Document> {
    const url = `${this.documentsUrl}/${docid}`;
    return this.http.get(url)
      .toPromise()
      .then(response => response.json().documents as Document)
      .catch(this.handleError);
  }

  private documentsUrl = sitnDocsConst['documentsUrl'];

  constructor(private http: Http) { }

  getDocuments(): Promise<Document[]> {
    return this.http.get(this.documentsUrl)
       .toPromise()
       .then(response => response.json().documents as Document[])
       .catch(this.handleError);
     }

  private headers = new Headers({'Content-Type': 'application/json'});

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }
}
