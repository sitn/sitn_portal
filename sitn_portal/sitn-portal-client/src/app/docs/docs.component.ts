import { Component, OnInit } from '@angular/core';

import { Document } from './document';
import { DocumentService } from './document.service';

@Component({
  selector: 'docs-root',
  templateUrl: './docs.component.html',
  styleUrls: ['./docs.component.css']
})

export class DocsComponent implements OnInit {

  documents: Document[];

  constructor(
    private documentService: DocumentService
  ) { }

  getDocuments(): void {
    this.documentService.getDocuments().then(documents => {
      this.documents = documents;
    });
  }

  ngOnInit(): void {
    this.getDocuments();
  }
}
