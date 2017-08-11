import { Component } from '@angular/core';

import { Document }    from './document';

@Component({
  selector: 'document-form',
  templateUrl: './document-form.component.html',
  styleUrls: [ './document-form.component.css' ],
})
export class DocumentFormComponent {

  doctype = [0, 1, 2];
  legalstate = [0, 1, 2];
  languages = ['de', 'en', 'fr', 'it', 'rm']
  states = ['AI', 'AG', 'AR', 'BS', 'BL', 'NE'];

  model = new Document(
    'NETST00100000001',
    this.doctype[1],
    this.languages[2],
    this.states[5],
    'Test document',
    '01.01.2017',
    '01.01.2017',
    this.legalstate[2],
    'voisardf');

  submitted = false;

  onSubmit() { this.submitted = true; }

  // TODO: Remove this when we're done
  //get diagnostic() { return JSON.stringify(this.model); }
}
