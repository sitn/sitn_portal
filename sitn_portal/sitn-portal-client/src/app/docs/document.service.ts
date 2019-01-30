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

  private headers = new Headers({'Content-Type': 'application/x-www-form-urlencoded'});

  constructor(private http: Http) { }

  getDocument(docid: string): Promise<Document> {
    const url = `${this.documentsUrl}/get/${docid}`;
    return this.http.get(url)
      .toPromise()
      .then(response => response.json().document as Document)
      .catch(this.handleError);
  }

  getDocuments(): Promise<Document[]> {
    const url = `${this.documentsUrl}/list`;
    return this.http.get(url)
       .toPromise()
       .then(response => response.json().documents as Document[])
       .catch(this.handleError);
     }

    addDocument(document: Document): Promise<Document> {
       const url = `${this.documentsUrl}/add`;
       return this.http
       .post(url, {'document': document}, {headers: this.headers})
       .toPromise()
       .then(response => document as Document)
       .catch(this.handleError);
    }

    editDocument(document: Document): Promise<Document> {
      const url = `${this.documentsUrl}/edit`;
      return this.http
        .put(url, JSON.stringify(document), {headers: this.headers})
        .toPromise()
        .then(() => document)
        .catch(this.handleError);
    }

    deleteDocument(docid: string): Promise<void> {
      const url = `${this.documentsUrl}/delete/${docid}`;
      return this.http.delete(url, {headers: this.headers})
        .toPromise()
        .then(() => null)
        .catch(this.handleError);
    }

}
