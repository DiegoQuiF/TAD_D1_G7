import { TestBed } from '@angular/core/testing';

import { ConnBackendService } from './conn-backend.service';

describe('ConnBackendService', () => {
  let service: ConnBackendService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ConnBackendService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
