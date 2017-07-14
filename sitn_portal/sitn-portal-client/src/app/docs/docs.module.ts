import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { DocsComponent } from './docs.component';

@NgModule({
  declarations: [
    DocsComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [DocsComponent]
})
export class DocsModule { }
