bool my_access(struct stat *statbuf, int mode){
  bool r = 0,w = 0,x = 0;  // boolean set if got this access
  if(getuid() == statbuf->st_uid){
     if( statbuf->st_mode & 00400 == 00400){
       r = 1;
     }
     if ( statbuf->st_mode & 00200 == 00200){
       w = 1;
     }
     if( statbuf->st_mode & 00100 == 00100){
       e = 1;
     }
  }

  g_idt *list = malloc(sizeof(g_idt) * BUFFSIZE);
  int numOfGroups = getgroups(BUFFSIZE, list);

  for(int i = 0; i < numOfGroups; i++){
    if(list[i] == statbuf->st_gid){
     if( statbuf->st_mode & 00040 == 00040){
       r = 1;
     }
     if ( statbuf->st_mode & 00020 == 00020){
       w = 1;
     }
     if( statbuf->st_mode & 00010 == 00010){
       e = 1;
     }
    }
  }

  if( statbuf->st_mode & 00004 == 00004){
    r = 1;
  }
  if ( statbuf->st_mode & 00002 == 00002){
    w = 1;
  }
  if( statbuf->st_mode & 00001 == 00001){
    e = 1;
  }


    bool result = 1;
    if(mode & R_OK == R_OK){
      result &= r;
    }

    if(mode & W_OK == W_OK){
      result &= w;
    }

    if(mode & X_OK == X_OK){
      result &= x;
    }

  return result;
}
