import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';

import { Document } from './document';

declare var sitnDocsConst:object;

@Injectable()
export class DocumentService {

  private documentsUrl = sitnDocsConst['documentsUrl'];

  private handleError(error: any): Promise<any> {
    return Promise.reject(error.message || error);
  }
  constructor(private http: Http) { }

  getDocument(docid: string): Promise<Document> {
    const url = `${this.documentsUrl}/get/${docid}`;
    return this.http.get(url)
      .toPromise()
      .then(response => response.json().documents as Document)
      .catch(this.handleError);
  }

  getDocuments(): Promise<Document[]> {
    const url = `${this.documentsUrl}/list`;
    return this.http.get(url)
       .toPromise()
       .then(response => response.json().documents as Document[])
       .catch(this.handleError);
     }
}
