import { Component, OnInit} from '@angular/core';
import { Router } from '@angular/router'
import { Document } from './document';
import { DocumentService } from './document.service';

@Component({
  selector: 'document-list',
  templateUrl: './document-list.component.html',
  styleUrls: ['./document-list.component.css']
})

export class DocumentListComponent implements OnInit {
  documents: Document[];
  selectedDocument: Document;

  constructor(
    private documentService: DocumentService,
    private router: Router) { }

  ngOnInit(): void {
    this.getDocuments();
  }

  onSelect(document: Document): void {
      this.selectedDocument = document;
  }

  getDocuments(): void {
    this.documentService.getDocuments().then(documents => this.documents = documents);
  }

  gotoDetail(): void {
    this.router.navigate(['/docdetail', this.selectedDocument.docid]);
  }

 }
