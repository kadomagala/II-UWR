#include "csapp.h"

static __unused void outc(char c) {
  Write(STDOUT_FILENO, &c, 1);
}

static __thread unsigned seed;

static sem_t tobacco;
static sem_t matches;
static sem_t paper;
static sem_t doneSmoking;

/* TODO: If you need any extra global variables, then define them here. */

static bool isTobacco;
static bool isMatches;
static bool isPaper;

static sem_t pusher_m;
static sem_t tobacco_smoker;
static sem_t matches_smoker;
static sem_t paper_smoker;

static void *agent(void *arg) {
  seed = pthread_self();

  while (true) {
    Sem_wait(&doneSmoking);

    int choice = rand_r(&seed) % 3;
    if (choice == 0) {
      Sem_post(&tobacco);
      Sem_post(&paper);
    } else if (choice == 1) {
      Sem_post(&tobacco);
      Sem_post(&matches);
    } else {
      Sem_post(&paper);
      Sem_post(&matches);
    }
  }

  return NULL;
}

/* TODO: If you need extra threads, then define their main procedures here. */
static void *tobacco_pusher(void *arg) {

  while (true) {
    Sem_wait(&tobacco);
    Sem_wait(&pusher_m);
    
    if(isPaper){
      isPaper = false;
      Sem_post(&matches_smoker);
    }else if(isMatches){
      isMatches = false;
      Sem_post(&paper_smoker);
    }else{
      isTobacco = true;
    }

    Sem_post(&pusher_m);
  }

  return NULL;
}

static void *matches_pusher(void *arg) {

  while (true) {
    Sem_wait(&matches);
    Sem_wait(&pusher_m);
    
    if(isPaper){
      isPaper = false;
      Sem_post(&tobacco_smoker);
    }else if(isTobacco){
      isTobacco = false;
      Sem_post(&paper_smoker);
    }else{
      isMatches = true;
    }

    Sem_post(&pusher_m);
    
  }

  return NULL;
}

static void *paper_pusher(void *arg) {
 
  while (true) {
    Sem_wait(&paper);
    Sem_wait(&pusher_m);
    
    if(isTobacco){
      isTobacco = false;
      Sem_post(&matches_smoker);
    }else if(isMatches){
      isMatches = false;
      Sem_post(&tobacco_smoker);
    }else{
      isPaper = true;
    }

    Sem_post(&pusher_m);
    
  }

  return NULL;
}

static void randsleep(void) {
  usleep(rand_r(&seed) % 1000 + 1000);
}

static void make_and_smoke(char smoker) {
  randsleep();
  Sem_post(&doneSmoking);
  outc(smoker);
  randsleep();
}

static void *smokerWithMatches(void *arg) {
  seed = pthread_self();

  while (true) {
    /* TODO: wait for paper and tobacco */
    Sem_wait(&matches_smoker);
    make_and_smoke('M');
  }

  return NULL;
}

static void *smokerWithTobacco(void *arg) {
  seed = pthread_self();

  while (true) {
    /* TODO: wait for paper and matches */
    Sem_wait(&tobacco_smoker);
    make_and_smoke('T');
  }

  return NULL;
}

static void *smokerWithPaper(void *arg) {
  seed = pthread_self();
 
  while (true) {
    /* TODO: wait for tobacco and matches */
    Sem_wait(&paper_smoker);
    make_and_smoke('P');
  }

  return NULL;
}

int main(void) {
  Sem_init(&tobacco, 0, 0);
  Sem_init(&matches, 0, 0);
  Sem_init(&paper, 0, 0);
  Sem_init(&doneSmoking, 0, 1);
  

  /* TODO: Initialize your global variables here. */
  isPaper = isMatches = isTobacco = false;
  
  Sem_init(&matches_smoker, 0, 0);
  Sem_init(&tobacco_smoker, 0, 0);
  Sem_init(&paper_smoker, 0 ,0);
  Sem_init(&pusher_m, 0, 1);

  pthread_t pusher_tobacco, pusher_paper, pusher_matches;
  Pthread_create(&pusher_tobacco, NULL, tobacco_pusher, NULL);
  Pthread_create(&pusher_paper, NULL, paper_pusher, NULL);
  Pthread_create(&pusher_matches, NULL, matches_pusher, NULL);


  pthread_t agentThread;
  Pthread_create(&agentThread, NULL, agent, NULL);

  pthread_t smokerPaperThread, smokerMatchesThread, smokerTobaccoThread;
  Pthread_create(&smokerPaperThread, NULL, smokerWithPaper, NULL);
  Pthread_create(&smokerMatchesThread, NULL, smokerWithMatches, NULL);
  Pthread_create(&smokerTobaccoThread, NULL, smokerWithTobacco, NULL);

  Pthread_join(agentThread, NULL);
  Pthread_join(smokerPaperThread, NULL);
  Pthread_join(smokerMatchesThread, NULL);
  Pthread_join(smokerTobaccoThread, NULL);

  Pthread_join(pusher_tobacco, NULL);
  Pthread_join(pusher_matches, NULL);
  Pthread_join(pusher_paper, NULL);

  return 0;
}
