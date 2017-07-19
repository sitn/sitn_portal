import { TestBed, async } from '@angular/core/testing';

import {MyappComponent } from './myapp.component';

describe('MyappComponent', () => {
  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [
        MyappComponent
      ],
    }).compileComponents();
  }));

  it('should create the myapp app', async(() => {
    const fixture = TestBed.createComponent(MyappComponent);
    const app = fixture.debugElement.componentInstance;
    expect(app).toBeTruthy();
  }));

  it(`should have as title 'myapp'`, async(() => {
    const fixture = TestBed.createComponent(MyappComponent);
    const app = fixture.debugElement.componentInstance;
    expect(app.title).toEqual('myapp');
  }));

  it('should render title in a h1 tag', async(() => {
    const fixture = TestBed.createComponent(MyappComponent);
    fixture.detectChanges();
    const compiled = fixture.debugElement.nativeElement;
    expect(compiled.querySelector('h1').textContent).toContain('Welcome to myapp!!');
  }));
});
