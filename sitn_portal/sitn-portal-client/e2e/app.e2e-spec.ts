import { SitnPortalClientPage } from './app.po';

describe('sitn-portal-client App', () => {
  let page: SitnPortalClientPage;

  beforeEach(() => {
    page = new SitnPortalClientPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
