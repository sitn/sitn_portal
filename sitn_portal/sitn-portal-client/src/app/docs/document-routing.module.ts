import { NgModule }      from '@angular/core';
import { RouterModule, Routes } from '@angular/router'

import { DocumentFormComponent } from './document-form.component';
import { DocumentListComponent } from './document-list.component';
import { DocumentDetailComponent }     from './document-detail.component';
import { DocsComponent } from './docs.component';

const routes: Routes = [
  { path: '', redirectTo: '/documents', pathMatch: 'full' },
  { path: 'docform',  component: DocumentFormComponent },
  { path: 'docdetail/:docid', component: DocumentDetailComponent },
  { path: 'doclist',     component: DocumentListComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class DocumentRoutingModule {}
