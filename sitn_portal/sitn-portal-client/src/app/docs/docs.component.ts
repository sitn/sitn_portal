import { Component, OnInit } from '@angular/core';

import { Doc } from './doc';
import { DocService } from './doc.service';

@Component({
  selector: 'docs-root',
  templateUrl: './docs.component.html',
  styleUrls: ['./docs.component.css']
})

export class DocsComponent implements OnInit {

  docs: Doc[];
  title = 'docs';

  constructor(
    private docService: DocService
  ) { }

  getDocs(): void {
    this.docService.getDocs().then(docs => {
      this.docs = docs;
    });
  }

  ngOnInit(): void {
    this.getDocs();
  }
}
