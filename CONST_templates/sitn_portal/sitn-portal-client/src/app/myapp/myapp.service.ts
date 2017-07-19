import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

import 'rxjs/add/operator/toPromise';

import { Myapp } from './myapp';

declare var sitnMyappConst:object;

@Injectable()
export class DocService {

  constructor(
    private http: Http
  ) { }

  private myapp_fake_Url = sitnMyappConst['myapp_fake_Url'];

  getDocs(): Promise<Doc[]> {
    return this.http.get(this.myapp_fake_Url)
      .toPromise()
      .then(response => response.json().myapp as Myapp[])
      .catch(this.handleError);
  }

  private handleError(error: any): Promise<any> {
    console.error('A toto occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }
}
