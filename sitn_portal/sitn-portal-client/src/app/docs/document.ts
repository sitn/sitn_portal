export class Document  {
  constructor(
    public docid: string,
    public doctype: number,
    public lang: string,
    public state: string,
    public officialtitle: string,
    public entrydate: string,
    public publicationdate: string,
    public legalstate: number,
    public operator: string,
    public chmunicipalitynb?: number,
    public municipalitynb?: number,
    public municipalityname?: string,
    public cadastrenb?: number,
    public title?: string,
    public abbreviation?: string,
    public officialnb?: string,
    public remoteurl?: string,
    public localurl?: string,
    public sanctiondate?: string,
    public abolishingdate?: string,
    public revisiondate?: string,
    public effectivedate?: string,
    public approbationdate?: string
  ) {}
}
