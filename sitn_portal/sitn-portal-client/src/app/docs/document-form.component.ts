import { Component } from '@angular/core';

import { Document }    from './document';
import { DocumentService } from './document.service';

@Component({
  selector: 'document-form',
  templateUrl: './document-form.component.html',
  styleUrls: [ './document-form.component.css' ],
})
export class DocumentFormComponent {
  documents: Document[];
  selectedDocument: Document;

  doctype = [0, 1, 2];
  legalstate = [0, 1, 2];
  languages = ['de', 'en', 'fr', 'it', 'rm']
  states = ['AI', 'AG', 'AR', 'BS', 'BL', 'NE'];

  document = new Document(
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


  private handleError(error: any): Promise<any> {
    return Promise.reject(error.message || error);
  }

  constructor(private documentService: DocumentService) { }

  add(document: Document): void {
    if (!document) {return; }
    this.documentService.addDocument(document)
    .then(document => this.document = document)
    .catch(this.handleError);
  }
}
