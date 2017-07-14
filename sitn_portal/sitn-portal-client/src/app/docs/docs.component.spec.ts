import { TestBed, async } from '@angular/core/testing';

import { DocsComponent } from './docs.component';

describe('DocsComponent', () => {
  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [
        DocsComponent
      ],
    }).compileComponents();
  }));

  it('should create the docs app', async(() => {
    const fixture = TestBed.createComponent(DocsComponent);
    const app = fixture.debugElement.componentInstance;
    expect(app).toBeTruthy();
  }));

  it(`should have as title 'docs'`, async(() => {
    const fixture = TestBed.createComponent(DocsComponent);
    const app = fixture.debugElement.componentInstance;
    expect(app.title).toEqual('docs');
  }));

  it('should render title in a h1 tag', async(() => {
    const fixture = TestBed.createComponent(DocsComponent);
    fixture.detectChanges();
    const compiled = fixture.debugElement.nativeElement;
    expect(compiled.querySelector('h1').textContent).toContain('Welcome to docs!!');
  }));
});