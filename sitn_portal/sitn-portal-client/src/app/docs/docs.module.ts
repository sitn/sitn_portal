import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';

import { DocsComponent } from './docs.component';
import { DocService } from './doc.service';
import { DocGlobals } from './globals';

@NgModule({
  declarations: [
    DocsComponent
  ],

  imports: [
    BrowserModule,
    HttpModule
  ],

  providers: [
    DocService,
    DocGlobals
    ],

  bootstrap: [DocsComponent]

})
export class DocsModule { }
