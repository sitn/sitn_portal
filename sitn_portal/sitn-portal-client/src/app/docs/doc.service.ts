import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';

import { Doc } from './doc';

declare var sitnDocsConst:object;

@Injectable()
export class DocService {

  constructor(
    private http: Http
  ) { }

  private docs_fake_Url = sitnDocsConst['docs_fake_Url'];

  getDocs(): Promise<Doc[]> {
    return this.http.get(this.docs_fake_Url)
      .toPromise()
      .then(response => response.json().docs as Doc[])
      .catch(this.handleError);
  }

  private handleError(error: any): Promise<any> {
    console.error('A toto occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }
}
