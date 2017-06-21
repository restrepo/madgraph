      SUBROUTINE ML5_0_MP_COMPUTE_LOOP_COEFS(PS,ANSDP)
C     
C     Generated by MadGraph5_aMC@NLO v. %(version)s, %(date)s
C     By the MadGraph5_aMC@NLO Development Team
C     Visit launchpad.net/madgraph5 and amcatnlo.web.cern.ch
C     
C     Returns amplitude squared summed/avg over colors
C     and helicities for the point in phase space P(0:3,NEXTERNAL)
C     and external lines W(0:6,NEXTERNAL)
C     
C     Process: g g > t t~ QED=0 QCD=2 [ virt = QCD ]
C     
      IMPLICIT NONE
C     
C     CONSTANTS
C     
      CHARACTER*64 PARAMFILENAME
      PARAMETER ( PARAMFILENAME='MadLoopParams.dat')
      INTEGER NBORNAMPS
      PARAMETER (NBORNAMPS=3)
      INTEGER    NLOOPS, NLOOPGROUPS, NCTAMPS
      PARAMETER (NLOOPS=44, NLOOPGROUPS=26, NCTAMPS=85)
      INTEGER    NLOOPAMPS
      PARAMETER (NLOOPAMPS=129)
      INTEGER    NCOLORROWS
      PARAMETER (NCOLORROWS=NLOOPAMPS)
      INTEGER    NEXTERNAL
      PARAMETER (NEXTERNAL=4)
      INTEGER    NWAVEFUNCS,NLOOPWAVEFUNCS
      PARAMETER (NWAVEFUNCS=10,NLOOPWAVEFUNCS=93)
      INTEGER MAXLWFSIZE
      PARAMETER (MAXLWFSIZE=4)
      INTEGER LOOPMAXCOEFS, VERTEXMAXCOEFS
      PARAMETER (LOOPMAXCOEFS=35, VERTEXMAXCOEFS=5)
      INTEGER    NCOMB
      PARAMETER (NCOMB=16)
      REAL*16    ZERO
      PARAMETER (ZERO=0E0_16)
      COMPLEX*32 IMAG1
      PARAMETER (IMAG1=(0E0_16,1E0_16))
C     These are constants related to the split orders
      INTEGER    NSO, NSQUAREDSO, NAMPSO
      PARAMETER (NSO=0, NSQUAREDSO=0, NAMPSO=0)


C     
C     ARGUMENTS 
C     
      REAL*16 PS(0:3,NEXTERNAL)
      REAL*8 ANSDP(3,0:NSQUAREDSO)
C     
C     LOCAL VARIABLES 
C     
      LOGICAL DPW_COPIED
      INTEGER I,J,K,H,HEL_MULT,ITEMP
      REAL*16 TEMP2
      INTEGER NHEL(NEXTERNAL), IC(NEXTERNAL)
      REAL*16 P(0:3,NEXTERNAL)
      DATA IC/NEXTERNAL*1/
      REAL*16 ANS(3,0:NSQUAREDSO)
      COMPLEX*32 COEFS(MAXLWFSIZE,0:VERTEXMAXCOEFS-1,MAXLWFSIZE)
      COMPLEX*32 CFTOT
C     
C     FUNCTIONS
C     
      INTEGER ML5_0_ML5SOINDEX_FOR_BORN_AMP
      INTEGER ML5_0_ML5SOINDEX_FOR_LOOP_AMP
      INTEGER ML5_0_ML5SQSOINDEX
C     
C     GLOBAL VARIABLES
C     
      INCLUDE 'mp_coupl_same_name.inc'

      LOGICAL CHECKPHASE, HELDOUBLECHECKED
      COMMON/ML5_0_INIT/CHECKPHASE, HELDOUBLECHECKED

      INTEGER HELOFFSET
      INTEGER GOODHEL(NCOMB)
      LOGICAL GOODAMP(NSQUAREDSO,NLOOPGROUPS)
      COMMON/ML5_0_FILTERS/GOODAMP,GOODHEL,HELOFFSET

      INTEGER HELPICKED
      COMMON/ML5_0_HELCHOICE/HELPICKED

      INTEGER USERHEL
      COMMON/ML5_0_USERCHOICE/USERHEL

      INTEGER SQSO_TARGET
      COMMON/ML5_0_SOCHOICE/SQSO_TARGET

      LOGICAL UVCT_REQ_SO_DONE,MP_UVCT_REQ_SO_DONE,CT_REQ_SO_DONE
     $ ,MP_CT_REQ_SO_DONE,LOOP_REQ_SO_DONE,MP_LOOP_REQ_SO_DONE
     $ ,CTCALL_REQ_SO_DONE,FILTER_SO
      COMMON/ML5_0_SO_REQS/UVCT_REQ_SO_DONE,MP_UVCT_REQ_SO_DONE
     $ ,CT_REQ_SO_DONE,MP_CT_REQ_SO_DONE,LOOP_REQ_SO_DONE,MP_LOOP_REQ_S
     $ O_DONE,CTCALL_REQ_SO_DONE,FILTER_SO

      COMPLEX*32 AMP(NBORNAMPS)
      COMMON/ML5_0_MP_AMPS/AMP
      COMPLEX*16 DP_AMP(NBORNAMPS)
      COMMON/ML5_0_AMPS/DP_AMP
      COMPLEX*32 W(20,NWAVEFUNCS)
      COMMON/ML5_0_MP_W/W

      COMPLEX*16 DPW(20,NWAVEFUNCS)
      COMMON/ML5_0_W/DPW

      COMPLEX*32 WL(MAXLWFSIZE,0:LOOPMAXCOEFS-1,MAXLWFSIZE,0:NLOOPWAVEF
     $ UNCS)
      COMPLEX*32 PL(0:3,0:NLOOPWAVEFUNCS)
      COMMON/ML5_0_MP_WL/WL,PL

      COMPLEX*32 LOOPCOEFS(0:LOOPMAXCOEFS-1,NSQUAREDSO,NLOOPGROUPS)
      COMMON/ML5_0_MP_LCOEFS/LOOPCOEFS


      COMPLEX*32 AMPL(3,NCTAMPS)
      COMMON/ML5_0_MP_AMPL/AMPL


      INTEGER CF_D(NCOLORROWS,NBORNAMPS)
      INTEGER CF_N(NCOLORROWS,NBORNAMPS)
      COMMON/ML5_0_CF/CF_D,CF_N

      INTEGER HELC(NEXTERNAL,NCOMB)
      COMMON/ML5_0_HELCONFIGS/HELC

      LOGICAL MP_DONE_ONCE
      COMMON/ML5_0_MP_DONE_ONCE/MP_DONE_ONCE

C     ----------
C     BEGIN CODE
C     ----------

C     To be on the safe side, we always update the MP params here.
C     It can be redundant as this routine can be called a couple of
C      times for the same PS point during the stability checks.
C     But it is really not time consuming and I would rather be safe.
      CALL MP_UPDATE_AS_PARAM()

      MP_DONE_ONCE = .TRUE.

C     AS A SAFETY MEASURE WE FIRST COPY HERE THE PS POINT
      DO I=1,NEXTERNAL
        DO J=0,3
          P(J,I)=PS(J,I)
        ENDDO
      ENDDO

      DO I=0,3
        PL(I,0)=(ZERO,ZERO)
      ENDDO
      DO I=1,MAXLWFSIZE
        DO J=0,LOOPMAXCOEFS-1
          DO K=1,MAXLWFSIZE
            IF(I.EQ.K.AND.J.EQ.0) THEN
              WL(I,J,K,0)=(1.0E0_16,ZERO)
            ELSE
              WL(I,J,K,0)=(ZERO,ZERO)
            ENDIF
          ENDDO
        ENDDO
      ENDDO

      DO K=1, 3
        DO I=1,NCTAMPS
          AMPL(K,I)=(ZERO,ZERO)
        ENDDO
      ENDDO


      DO I=1, NBORNAMPS
        DP_AMP(I) = (0.0D0,0.0D0)
        AMP(I) = (ZERO, ZERO)
      ENDDO

      DO I=1,NLOOPGROUPS
        DO J=0,LOOPMAXCOEFS-1
          DO K=1,NSQUAREDSO
            LOOPCOEFS(J,K,I)=(ZERO,ZERO)
          ENDDO
        ENDDO
      ENDDO

      DO K=1,3
        DO J=0,NSQUAREDSO
          ANSDP(K,J)=0.0D0
          ANS(K,J)=ZERO
        ENDDO
      ENDDO

      DPW_COPIED = .FALSE.
      DO H=1,NCOMB
        IF ((HELPICKED.EQ.H).OR.((HELPICKED.EQ.-1).AND.(CHECKPHASE.OR.(
     $   .NOT.HELDOUBLECHECKED).OR.(GOODHEL(H).GT.-HELOFFSET.AND.GOODHE
     $   L(H).NE.0)))) THEN
          DO I=1,NEXTERNAL
            NHEL(I)=HELC(I,H)
          ENDDO

          MP_UVCT_REQ_SO_DONE=.FALSE.
          MP_CT_REQ_SO_DONE=.FALSE.
          MP_LOOP_REQ_SO_DONE=.FALSE.

          IF (.NOT.CHECKPHASE.AND.HELDOUBLECHECKED.AND.HELPICKED.EQ.
     $     -1) THEN
            HEL_MULT=GOODHEL(H)
          ELSE
            HEL_MULT=1
          ENDIF


          CALL MP_VXXXXX(P(0,1),ZERO,NHEL(1),-1*IC(1),W(1,1))
          CALL MP_VXXXXX(P(0,2),ZERO,NHEL(2),-1*IC(2),W(1,2))
          CALL MP_OXXXXX(P(0,3),MDL_MT,NHEL(3),+1*IC(3),W(1,3))
          CALL MP_IXXXXX(P(0,4),MDL_MT,NHEL(4),-1*IC(4),W(1,4))
          CALL MP_VVV1P0_1(W(1,1),W(1,2),GC_4,ZERO,ZERO,W(1,5))
C         Amplitude(s) for born diagram with ID 1
          CALL MP_FFV1_0(W(1,4),W(1,3),W(1,5),GC_5,AMP(1))
          CALL MP_FFV1_1(W(1,3),W(1,1),GC_5,MDL_MT,MDL_WT,W(1,6))
C         Amplitude(s) for born diagram with ID 2
          CALL MP_FFV1_0(W(1,4),W(1,6),W(1,2),GC_5,AMP(2))
          CALL MP_FFV1_2(W(1,4),W(1,1),GC_5,MDL_MT,MDL_WT,W(1,7))
C         Amplitude(s) for born diagram with ID 3
          CALL MP_FFV1_0(W(1,7),W(1,3),W(1,2),GC_5,AMP(3))
          CALL MP_FFV1P0_3(W(1,4),W(1,3),GC_5,ZERO,ZERO,W(1,8))
C         Counter-term amplitude(s) for loop diagram number 4
          CALL MP_R2_GG_1_0(W(1,5),W(1,8),R2_GGQ,AMPL(1,1))
          CALL MP_R2_GG_1_0(W(1,5),W(1,8),R2_GGQ,AMPL(1,2))
          CALL MP_R2_GG_1_0(W(1,5),W(1,8),R2_GGQ,AMPL(1,3))
          CALL MP_R2_GG_1_0(W(1,5),W(1,8),R2_GGQ,AMPL(1,4))
C         Counter-term amplitude(s) for loop diagram number 5
          CALL MP_VVV1_0(W(1,1),W(1,2),W(1,8),UV_3GB_1EPS,AMPL(2,5))
          CALL MP_VVV1_0(W(1,1),W(1,2),W(1,8),UV_3GB_1EPS,AMPL(2,6))
          CALL MP_VVV1_0(W(1,1),W(1,2),W(1,8),UV_3GB_1EPS,AMPL(2,7))
          CALL MP_VVV1_0(W(1,1),W(1,2),W(1,8),UV_3GB_1EPS,AMPL(2,8))
          CALL MP_VVV1_0(W(1,1),W(1,2),W(1,8),UV_3GB,AMPL(1,9))
          CALL MP_VVV1_0(W(1,1),W(1,2),W(1,8),UV_3GB_1EPS,AMPL(2,10))
          CALL MP_VVV1_0(W(1,1),W(1,2),W(1,8),UV_3GT,AMPL(1,11))
          CALL MP_VVV1_0(W(1,1),W(1,2),W(1,8),UV_3GB_1EPS,AMPL(2,12))
          CALL MP_VVV1_0(W(1,1),W(1,2),W(1,8),UV_3GG_1EPS,AMPL(2,13))
          CALL MP_VVV1_0(W(1,1),W(1,2),W(1,8),R2_3GQ,AMPL(1,14))
          CALL MP_VVV1_0(W(1,1),W(1,2),W(1,8),R2_3GQ,AMPL(1,15))
          CALL MP_VVV1_0(W(1,1),W(1,2),W(1,8),R2_3GQ,AMPL(1,16))
          CALL MP_VVV1_0(W(1,1),W(1,2),W(1,8),R2_3GQ,AMPL(1,17))
C         Counter-term amplitude(s) for loop diagram number 7
          CALL MP_R2_GG_1_R2_GG_3_0(W(1,5),W(1,8),R2_GGQ,R2_GGB,AMPL(1
     $     ,18))
C         Counter-term amplitude(s) for loop diagram number 8
          CALL MP_VVV1_0(W(1,1),W(1,2),W(1,8),R2_3GQ,AMPL(1,19))
C         Counter-term amplitude(s) for loop diagram number 10
          CALL MP_R2_GG_1_R2_GG_3_0(W(1,5),W(1,8),R2_GGQ,R2_GGT,AMPL(1
     $     ,20))
C         Counter-term amplitude(s) for loop diagram number 11
          CALL MP_FFV1_0(W(1,4),W(1,3),W(1,5),UV_GQQQ_1EPS,AMPL(2,21))
          CALL MP_FFV1_0(W(1,4),W(1,3),W(1,5),UV_GQQQ_1EPS,AMPL(2,22))
          CALL MP_FFV1_0(W(1,4),W(1,3),W(1,5),UV_GQQQ_1EPS,AMPL(2,23))
          CALL MP_FFV1_0(W(1,4),W(1,3),W(1,5),UV_GQQQ_1EPS,AMPL(2,24))
          CALL MP_FFV1_0(W(1,4),W(1,3),W(1,5),UV_GQQB,AMPL(1,25))
          CALL MP_FFV1_0(W(1,4),W(1,3),W(1,5),UV_GQQQ_1EPS,AMPL(2,26))
          CALL MP_FFV1_0(W(1,4),W(1,3),W(1,5),UV_GQQT,AMPL(1,27))
          CALL MP_FFV1_0(W(1,4),W(1,3),W(1,5),UV_GQQQ_1EPS,AMPL(2,28))
          CALL MP_FFV1_0(W(1,4),W(1,3),W(1,5),UV_GQQG_1EPS,AMPL(2,29))
          CALL MP_FFV1_0(W(1,4),W(1,3),W(1,5),R2_GQQ,AMPL(1,30))
          CALL MP_FFV1_2(W(1,4),W(1,2),GC_5,MDL_MT,MDL_WT,W(1,9))
C         Counter-term amplitude(s) for loop diagram number 13
          CALL MP_R2_QQ_1_R2_QQ_2_0(W(1,9),W(1,6),R2_QQQ,R2_QQT,AMPL(1
     $     ,31))
          CALL MP_R2_QQ_2_0(W(1,9),W(1,6),UV_TMASS,AMPL(1,32))
          CALL MP_R2_QQ_2_0(W(1,9),W(1,6),UV_TMASS_1EPS,AMPL(2,33))
C         Counter-term amplitude(s) for loop diagram number 14
          CALL MP_FFV1_0(W(1,4),W(1,6),W(1,2),UV_GQQQ_1EPS,AMPL(2,34))
          CALL MP_FFV1_0(W(1,4),W(1,6),W(1,2),UV_GQQQ_1EPS,AMPL(2,35))
          CALL MP_FFV1_0(W(1,4),W(1,6),W(1,2),UV_GQQQ_1EPS,AMPL(2,36))
          CALL MP_FFV1_0(W(1,4),W(1,6),W(1,2),UV_GQQQ_1EPS,AMPL(2,37))
          CALL MP_FFV1_0(W(1,4),W(1,6),W(1,2),UV_GQQB,AMPL(1,38))
          CALL MP_FFV1_0(W(1,4),W(1,6),W(1,2),UV_GQQQ_1EPS,AMPL(2,39))
          CALL MP_FFV1_0(W(1,4),W(1,6),W(1,2),UV_GQQT,AMPL(1,40))
          CALL MP_FFV1_0(W(1,4),W(1,6),W(1,2),UV_GQQQ_1EPS,AMPL(2,41))
          CALL MP_FFV1_0(W(1,4),W(1,6),W(1,2),UV_GQQG_1EPS,AMPL(2,42))
          CALL MP_FFV1_0(W(1,4),W(1,6),W(1,2),R2_GQQ,AMPL(1,43))
          CALL MP_FFV1_1(W(1,3),W(1,2),GC_5,MDL_MT,MDL_WT,W(1,10))
C         Counter-term amplitude(s) for loop diagram number 16
          CALL MP_R2_QQ_1_R2_QQ_2_0(W(1,7),W(1,10),R2_QQQ,R2_QQT
     $     ,AMPL(1,44))
          CALL MP_R2_QQ_2_0(W(1,7),W(1,10),UV_TMASS,AMPL(1,45))
          CALL MP_R2_QQ_2_0(W(1,7),W(1,10),UV_TMASS_1EPS,AMPL(2,46))
C         Counter-term amplitude(s) for loop diagram number 17
          CALL MP_FFV1_0(W(1,7),W(1,3),W(1,2),UV_GQQQ_1EPS,AMPL(2,47))
          CALL MP_FFV1_0(W(1,7),W(1,3),W(1,2),UV_GQQQ_1EPS,AMPL(2,48))
          CALL MP_FFV1_0(W(1,7),W(1,3),W(1,2),UV_GQQQ_1EPS,AMPL(2,49))
          CALL MP_FFV1_0(W(1,7),W(1,3),W(1,2),UV_GQQQ_1EPS,AMPL(2,50))
          CALL MP_FFV1_0(W(1,7),W(1,3),W(1,2),UV_GQQB,AMPL(1,51))
          CALL MP_FFV1_0(W(1,7),W(1,3),W(1,2),UV_GQQQ_1EPS,AMPL(2,52))
          CALL MP_FFV1_0(W(1,7),W(1,3),W(1,2),UV_GQQT,AMPL(1,53))
          CALL MP_FFV1_0(W(1,7),W(1,3),W(1,2),UV_GQQQ_1EPS,AMPL(2,54))
          CALL MP_FFV1_0(W(1,7),W(1,3),W(1,2),UV_GQQG_1EPS,AMPL(2,55))
          CALL MP_FFV1_0(W(1,7),W(1,3),W(1,2),R2_GQQ,AMPL(1,56))
C         Counter-term amplitude(s) for loop diagram number 19
          CALL MP_FFV1_0(W(1,4),W(1,10),W(1,1),UV_GQQQ_1EPS,AMPL(2,57))
          CALL MP_FFV1_0(W(1,4),W(1,10),W(1,1),UV_GQQQ_1EPS,AMPL(2,58))
          CALL MP_FFV1_0(W(1,4),W(1,10),W(1,1),UV_GQQQ_1EPS,AMPL(2,59))
          CALL MP_FFV1_0(W(1,4),W(1,10),W(1,1),UV_GQQQ_1EPS,AMPL(2,60))
          CALL MP_FFV1_0(W(1,4),W(1,10),W(1,1),UV_GQQB,AMPL(1,61))
          CALL MP_FFV1_0(W(1,4),W(1,10),W(1,1),UV_GQQQ_1EPS,AMPL(2,62))
          CALL MP_FFV1_0(W(1,4),W(1,10),W(1,1),UV_GQQT,AMPL(1,63))
          CALL MP_FFV1_0(W(1,4),W(1,10),W(1,1),UV_GQQQ_1EPS,AMPL(2,64))
          CALL MP_FFV1_0(W(1,4),W(1,10),W(1,1),UV_GQQG_1EPS,AMPL(2,65))
          CALL MP_FFV1_0(W(1,4),W(1,10),W(1,1),R2_GQQ,AMPL(1,66))
C         Counter-term amplitude(s) for loop diagram number 20
          CALL MP_FFV1_0(W(1,9),W(1,3),W(1,1),UV_GQQQ_1EPS,AMPL(2,67))
          CALL MP_FFV1_0(W(1,9),W(1,3),W(1,1),UV_GQQQ_1EPS,AMPL(2,68))
          CALL MP_FFV1_0(W(1,9),W(1,3),W(1,1),UV_GQQQ_1EPS,AMPL(2,69))
          CALL MP_FFV1_0(W(1,9),W(1,3),W(1,1),UV_GQQQ_1EPS,AMPL(2,70))
          CALL MP_FFV1_0(W(1,9),W(1,3),W(1,1),UV_GQQB,AMPL(1,71))
          CALL MP_FFV1_0(W(1,9),W(1,3),W(1,1),UV_GQQQ_1EPS,AMPL(2,72))
          CALL MP_FFV1_0(W(1,9),W(1,3),W(1,1),UV_GQQT,AMPL(1,73))
          CALL MP_FFV1_0(W(1,9),W(1,3),W(1,1),UV_GQQQ_1EPS,AMPL(2,74))
          CALL MP_FFV1_0(W(1,9),W(1,3),W(1,1),UV_GQQG_1EPS,AMPL(2,75))
          CALL MP_FFV1_0(W(1,9),W(1,3),W(1,1),R2_GQQ,AMPL(1,76))
C         Counter-term amplitude(s) for loop diagram number 22
          CALL MP_VVV1_0(W(1,1),W(1,2),W(1,8),R2_3GQ,AMPL(1,77))
C         Counter-term amplitude(s) for loop diagram number 32
          CALL MP_R2_GG_1_R2_GG_2_0(W(1,5),W(1,8),R2_GGG_1,R2_GGG_2
     $     ,AMPL(1,78))
C         Counter-term amplitude(s) for loop diagram number 33
          CALL MP_VVV1_0(W(1,1),W(1,2),W(1,8),R2_3GG,AMPL(1,79))
 2000     CONTINUE
          MP_CT_REQ_SO_DONE=.TRUE.

C         Amplitude(s) for UVCT diagram with ID 40
          CALL MP_FFV1_0(W(1,4),W(1,3),W(1,5),GC_5,AMPL(1,80))
          AMPL(1,80)=AMPL(1,80)*(2.0D0*UVWFCT_G_2+2.0D0*UVWFCT_G_1
     $     +2.0D0*UVWFCT_T_0)
C         Amplitude(s) for UVCT diagram with ID 41
          CALL MP_FFV1_0(W(1,4),W(1,3),W(1,5),GC_5,AMPL(2,81))
          AMPL(2,81)=AMPL(2,81)*(2.0D0*UVWFCT_B_0_1EPS+4.0D0*UVWFCT_G_2
     $     _1EPS)
C         Amplitude(s) for UVCT diagram with ID 42
          CALL MP_FFV1_0(W(1,4),W(1,6),W(1,2),GC_5,AMPL(1,82))
          AMPL(1,82)=AMPL(1,82)*(2.0D0*UVWFCT_G_2+2.0D0*UVWFCT_G_1
     $     +2.0D0*UVWFCT_T_0)
C         Amplitude(s) for UVCT diagram with ID 43
          CALL MP_FFV1_0(W(1,4),W(1,6),W(1,2),GC_5,AMPL(2,83))
          AMPL(2,83)=AMPL(2,83)*(2.0D0*UVWFCT_B_0_1EPS+4.0D0*UVWFCT_G_2
     $     _1EPS)
C         Amplitude(s) for UVCT diagram with ID 44
          CALL MP_FFV1_0(W(1,7),W(1,3),W(1,2),GC_5,AMPL(1,84))
          AMPL(1,84)=AMPL(1,84)*(2.0D0*UVWFCT_G_2+2.0D0*UVWFCT_G_1
     $     +2.0D0*UVWFCT_T_0)
C         Amplitude(s) for UVCT diagram with ID 45
          CALL MP_FFV1_0(W(1,7),W(1,3),W(1,2),GC_5,AMPL(2,85))
          AMPL(2,85)=AMPL(2,85)*(2.0D0*UVWFCT_B_0_1EPS+4.0D0*UVWFCT_G_2
     $     _1EPS)
 3000     CONTINUE
          MP_UVCT_REQ_SO_DONE=.TRUE.

          DO I=1,NCTAMPS
            DO J=1,NBORNAMPS
              CFTOT=CMPLX(CF_N(I,J)/REAL(ABS(CF_D(I,J)),KIND=16)
     $         ,0.0E0_16,KIND=16)
              IF(CF_D(I,J).LT.0) CFTOT=CFTOT*IMAG1
              ITEMP = ML5_0_ML5SQSOINDEX(ML5_0_ML5SOINDEX_FOR_LOOP_AMP(
     $         I),ML5_0_ML5SOINDEX_FOR_BORN_AMP(J))
              IF (.NOT.FILTER_SO.OR.SQSO_TARGET.EQ.ITEMP) THEN
                DO K=1,3
                  TEMP2 = HEL_MULT*2.0E0_16*REAL(CFTOT*AMPL(K,I)
     $             *CONJG(AMP(J)),KIND=16)
                  ANS(K,ITEMP)=ANS(K,ITEMP)+TEMP2
                  ANS(K,0)=ANS(K,0)+TEMP2
                ENDDO
              ENDIF
            ENDDO
          ENDDO

C         Coefficient construction for loop diagram with ID 4
          CALL MP_FFV1L2_1(PL(0,0),W(1,5),GC_5,ZERO,ZERO,PL(0,1),COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,1))
          CALL MP_FFV1L2_1(PL(0,1),W(1,8),GC_5,ZERO,ZERO,PL(0,2),COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,1),4,COEFS,4,4,WL(1,0,1
     $     ,2))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,2),2,4,1,1,4,86,H)
C         Coefficient construction for loop diagram with ID 5
          CALL MP_FFV1L1_2(PL(0,0),W(1,1),GC_5,ZERO,ZERO,PL(0,3),COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,3))
          CALL MP_FFV1L1_2(PL(0,3),W(1,2),GC_5,ZERO,ZERO,PL(0,4),COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,3),4,COEFS,4,4,WL(1,0,1
     $     ,4))
          CALL MP_FFV1L1_2(PL(0,4),W(1,8),GC_5,ZERO,ZERO,PL(0,5),COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_1(WL(1,0,1,4),4,COEFS,4,4,WL(1,0,1
     $     ,5))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,5),3,4,2,1,4,87,H)
C         Coefficient construction for loop diagram with ID 6
          CALL MP_FFV1L2_1(PL(0,0),W(1,1),GC_5,ZERO,ZERO,PL(0,6),COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,6))
          CALL MP_FFV1L2_1(PL(0,6),W(1,2),GC_5,ZERO,ZERO,PL(0,7),COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,6),4,COEFS,4,4,WL(1,0,1
     $     ,7))
          CALL MP_FFV1L2_1(PL(0,7),W(1,8),GC_5,ZERO,ZERO,PL(0,8),COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_1(WL(1,0,1,7),4,COEFS,4,4,WL(1,0,1
     $     ,8))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,8),3,4,2,1,4,88,H)
C         Coefficient construction for loop diagram with ID 7
          CALL MP_FFV1L2_1(PL(0,0),W(1,5),GC_5,MDL_MB,ZERO,PL(0,9)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,9))
          CALL MP_FFV1L2_1(PL(0,9),W(1,8),GC_5,MDL_MB,ZERO,PL(0,10)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,9),4,COEFS,4,4,WL(1,0,1
     $     ,10))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,10),2,4,3,1,1,89,H)
C         Coefficient construction for loop diagram with ID 8
          CALL MP_FFV1L1_2(PL(0,0),W(1,1),GC_5,MDL_MB,ZERO,PL(0,11)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,11))
          CALL MP_FFV1L1_2(PL(0,11),W(1,2),GC_5,MDL_MB,ZERO,PL(0,12)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,11),4,COEFS,4,4,WL(1,0
     $     ,1,12))
          CALL MP_FFV1L1_2(PL(0,12),W(1,8),GC_5,MDL_MB,ZERO,PL(0,13)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_1(WL(1,0,1,12),4,COEFS,4,4,WL(1,0
     $     ,1,13))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,13),3,4,4,1,1,90,H)
C         Coefficient construction for loop diagram with ID 9
          CALL MP_FFV1L2_1(PL(0,0),W(1,1),GC_5,MDL_MB,ZERO,PL(0,14)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,14))
          CALL MP_FFV1L2_1(PL(0,14),W(1,2),GC_5,MDL_MB,ZERO,PL(0,15)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,14),4,COEFS,4,4,WL(1,0
     $     ,1,15))
          CALL MP_FFV1L2_1(PL(0,15),W(1,8),GC_5,MDL_MB,ZERO,PL(0,16)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_1(WL(1,0,1,15),4,COEFS,4,4,WL(1,0
     $     ,1,16))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,16),3,4,4,1,1,91,H)
C         Coefficient construction for loop diagram with ID 10
          CALL MP_FFV1L2_1(PL(0,0),W(1,5),GC_5,MDL_MT,MDL_WT,PL(0,17)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,17))
          CALL MP_FFV1L2_1(PL(0,17),W(1,8),GC_5,MDL_MT,MDL_WT,PL(0,18)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,17),4,COEFS,4,4,WL(1,0
     $     ,1,18))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,18),2,4,5,1,1,92,H)
C         Coefficient construction for loop diagram with ID 11
          CALL MP_FFV1L1P0_3(PL(0,0),W(1,3),GC_5,ZERO,ZERO,PL(0,19)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_0(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,19))
          CALL MP_FFV1L3_2(PL(0,19),W(1,4),GC_5,MDL_MT,MDL_WT,PL(0,20)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,19),4,COEFS,4,4,WL(1,0
     $     ,1,20))
          CALL MP_FFV1L1_2(PL(0,20),W(1,5),GC_5,MDL_MT,MDL_WT,PL(0,21)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,20),4,COEFS,4,4,WL(1,0
     $     ,1,21))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,21),2,4,6,1,1,93,H)
C         Coefficient construction for loop diagram with ID 12
          CALL MP_FFV1L3_1(PL(0,0),W(1,3),GC_5,MDL_MT,MDL_WT,PL(0,22)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,22))
          CALL MP_FFV1L2P0_3(PL(0,22),W(1,4),GC_5,ZERO,ZERO,PL(0,23)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_0(WL(1,0,1,22),4,COEFS,4,4,WL(1,0
     $     ,1,23))
          CALL MP_VVV1L2P0_1(PL(0,23),W(1,5),GC_4,ZERO,ZERO,PL(0,24)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,23),4,COEFS,4,4,WL(1,0
     $     ,1,24))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,24),2,4,7,1,1,94,H)
C         Coefficient construction for loop diagram with ID 13
          CALL MP_FFV1L1P0_3(PL(0,0),W(1,6),GC_5,ZERO,ZERO,PL(0,25)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_0(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,25))
          CALL MP_FFV1L3_2(PL(0,25),W(1,9),GC_5,MDL_MT,MDL_WT,PL(0,26)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,25),4,COEFS,4,4,WL(1,0
     $     ,1,26))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,26),1,4,8,1,1,95,H)
C         Coefficient construction for loop diagram with ID 14
          CALL MP_FFV1L2_1(PL(0,0),W(1,2),GC_5,MDL_MT,MDL_WT,PL(0,27)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,27))
          CALL MP_FFV1L2P0_3(PL(0,27),W(1,4),GC_5,ZERO,ZERO,PL(0,28)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_0(WL(1,0,1,27),4,COEFS,4,4,WL(1,0
     $     ,1,28))
          CALL MP_FFV1L3_1(PL(0,28),W(1,6),GC_5,MDL_MT,MDL_WT,PL(0,29)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,28),4,COEFS,4,4,WL(1,0
     $     ,1,29))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,29),2,4,9,1,1,96,H)
C         Coefficient construction for loop diagram with ID 15
          CALL MP_VVV1L2P0_1(PL(0,0),W(1,2),GC_4,ZERO,ZERO,PL(0,30)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,30))
          CALL MP_FFV1L3_2(PL(0,30),W(1,4),GC_5,MDL_MT,MDL_WT,PL(0,31)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,30),4,COEFS,4,4,WL(1,0
     $     ,1,31))
          CALL MP_FFV1L1P0_3(PL(0,31),W(1,6),GC_5,ZERO,ZERO,PL(0,32)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_0(WL(1,0,1,31),4,COEFS,4,4,WL(1,0
     $     ,1,32))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,32),2,4,10,1,1,97,H)
C         Coefficient construction for loop diagram with ID 16
          CALL MP_FFV1L1P0_3(PL(0,0),W(1,10),GC_5,ZERO,ZERO,PL(0,33)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_0(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,33))
          CALL MP_FFV1L3_2(PL(0,33),W(1,7),GC_5,MDL_MT,MDL_WT,PL(0,34)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,33),4,COEFS,4,4,WL(1,0
     $     ,1,34))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,34),1,4,11,1,1,98,H)
C         Coefficient construction for loop diagram with ID 17
          CALL MP_FFV1L1_2(PL(0,0),W(1,2),GC_5,MDL_MT,MDL_WT,PL(0,35)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,35))
          CALL MP_FFV1L1P0_3(PL(0,35),W(1,3),GC_5,ZERO,ZERO,PL(0,36)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_0(WL(1,0,1,35),4,COEFS,4,4,WL(1,0
     $     ,1,36))
          CALL MP_FFV1L3_2(PL(0,36),W(1,7),GC_5,MDL_MT,MDL_WT,PL(0,37)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,36),4,COEFS,4,4,WL(1,0
     $     ,1,37))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,37),2,4,12,1,1,99,H)
C         Coefficient construction for loop diagram with ID 18
          CALL MP_FFV1L3_1(PL(0,30),W(1,3),GC_5,MDL_MT,MDL_WT,PL(0,38)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,30),4,COEFS,4,4,WL(1,0
     $     ,1,38))
          CALL MP_FFV1L2P0_3(PL(0,38),W(1,7),GC_5,ZERO,ZERO,PL(0,39)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_0(WL(1,0,1,38),4,COEFS,4,4,WL(1,0
     $     ,1,39))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,39),2,4,13,1,1,100
     $     ,H)
C         Coefficient construction for loop diagram with ID 19
          CALL MP_FFV1L2_1(PL(0,0),W(1,1),GC_5,MDL_MT,MDL_WT,PL(0,40)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,40))
          CALL MP_FFV1L2P0_3(PL(0,40),W(1,4),GC_5,ZERO,ZERO,PL(0,41)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_0(WL(1,0,1,40),4,COEFS,4,4,WL(1,0
     $     ,1,41))
          CALL MP_FFV1L3_1(PL(0,41),W(1,10),GC_5,MDL_MT,MDL_WT,PL(0
     $     ,42),COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,41),4,COEFS,4,4,WL(1,0
     $     ,1,42))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,42),2,4,14,1,1,101
     $     ,H)
C         Coefficient construction for loop diagram with ID 20
          CALL MP_FFV1L1_2(PL(0,0),W(1,1),GC_5,MDL_MT,MDL_WT,PL(0,43)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,43))
          CALL MP_FFV1L1P0_3(PL(0,43),W(1,3),GC_5,ZERO,ZERO,PL(0,44)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_0(WL(1,0,1,43),4,COEFS,4,4,WL(1,0
     $     ,1,44))
          CALL MP_FFV1L3_2(PL(0,44),W(1,9),GC_5,MDL_MT,MDL_WT,PL(0,45)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,44),4,COEFS,4,4,WL(1,0
     $     ,1,45))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,45),2,4,15,1,1,102
     $     ,H)
C         Coefficient construction for loop diagram with ID 21
          CALL MP_FFV1L1_2(PL(0,43),W(1,2),GC_5,MDL_MT,MDL_WT,PL(0,46)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,43),4,COEFS,4,4,WL(1,0
     $     ,1,46))
          CALL MP_FFV1L1P0_3(PL(0,46),W(1,3),GC_5,ZERO,ZERO,PL(0,47)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_0(WL(1,0,1,46),4,COEFS,4,4,WL(1,0
     $     ,1,47))
          CALL MP_FFV1L3_2(PL(0,47),W(1,4),GC_5,MDL_MT,MDL_WT,PL(0,48)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_1(WL(1,0,1,47),4,COEFS,4,4,WL(1,0
     $     ,1,48))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,48),3,4,16,1,1,103
     $     ,H)
C         Coefficient construction for loop diagram with ID 22
          CALL MP_FFV1L1_2(PL(0,46),W(1,8),GC_5,MDL_MT,MDL_WT,PL(0,49)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_1(WL(1,0,1,46),4,COEFS,4,4,WL(1,0
     $     ,1,49))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,49),3,4,17,1,1,104
     $     ,H)
C         Coefficient construction for loop diagram with ID 23
          CALL MP_FFV1L2_1(PL(0,40),W(1,2),GC_5,MDL_MT,MDL_WT,PL(0,50)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,40),4,COEFS,4,4,WL(1,0
     $     ,1,50))
          CALL MP_FFV1L2_1(PL(0,50),W(1,8),GC_5,MDL_MT,MDL_WT,PL(0,51)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_1(WL(1,0,1,50),4,COEFS,4,4,WL(1,0
     $     ,1,51))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,51),3,4,17,1,1,105
     $     ,H)
C         Coefficient construction for loop diagram with ID 24
          CALL MP_FFV1L2P0_3(PL(0,50),W(1,4),GC_5,ZERO,ZERO,PL(0,52)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_0(WL(1,0,1,50),4,COEFS,4,4,WL(1,0
     $     ,1,52))
          CALL MP_FFV1L3_1(PL(0,52),W(1,3),GC_5,MDL_MT,MDL_WT,PL(0,53)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_1(WL(1,0,1,52),4,COEFS,4,4,WL(1,0
     $     ,1,53))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,53),3,4,18,1,1,106
     $     ,H)
C         Coefficient construction for loop diagram with ID 25
          CALL MP_VVV1L2P0_1(PL(0,44),W(1,2),GC_4,ZERO,ZERO,PL(0,54)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,44),4,COEFS,4,4,WL(1,0
     $     ,1,54))
          CALL MP_FFV1L3_2(PL(0,54),W(1,4),GC_5,MDL_MT,MDL_WT,PL(0,55)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_1(WL(1,0,1,54),4,COEFS,4,4,WL(1,0
     $     ,1,55))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,55),3,4,19,1,1,107
     $     ,H)
C         Coefficient construction for loop diagram with ID 26
          CALL MP_VVV1L2P0_1(PL(0,0),W(1,1),GC_4,ZERO,ZERO,PL(0,56)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,56))
          CALL MP_FFV1L3_2(PL(0,56),W(1,4),GC_5,MDL_MT,MDL_WT,PL(0,57)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,56),4,COEFS,4,4,WL(1,0
     $     ,1,57))
          CALL MP_FFV1L1P0_3(PL(0,57),W(1,10),GC_5,ZERO,ZERO,PL(0,58)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_0(WL(1,0,1,57),4,COEFS,4,4,WL(1,0
     $     ,1,58))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,58),2,4,20,1,1,108
     $     ,H)
C         Coefficient construction for loop diagram with ID 27
          CALL MP_FFV1L3_1(PL(0,56),W(1,3),GC_5,MDL_MT,MDL_WT,PL(0,59)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,56),4,COEFS,4,4,WL(1,0
     $     ,1,59))
          CALL MP_FFV1L2P0_3(PL(0,59),W(1,9),GC_5,ZERO,ZERO,PL(0,60)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_0(WL(1,0,1,59),4,COEFS,4,4,WL(1,0
     $     ,1,60))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,60),2,4,21,1,1,109
     $     ,H)
C         Coefficient construction for loop diagram with ID 28
          CALL MP_FFV1L2_1(PL(0,59),W(1,2),GC_5,MDL_MT,MDL_WT,PL(0,61)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_1(WL(1,0,1,59),4,COEFS,4,4,WL(1,0
     $     ,1,61))
          CALL MP_FFV1L2P0_3(PL(0,61),W(1,4),GC_5,ZERO,ZERO,PL(0,62)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_3_0(WL(1,0,1,61),4,COEFS,4,4,WL(1,0
     $     ,1,62))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,62),3,4,22,1,1,110
     $     ,H)
C         Coefficient construction for loop diagram with ID 29
          CALL MP_VVVV1L2P0_1(PL(0,23),W(1,1),W(1,2),GC_6,ZERO,ZERO
     $     ,PL(0,63),COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_0(WL(1,0,1,23),4,COEFS,4,4,WL(1,0
     $     ,1,63))
          CALL MP_VVVV3L2P0_1(PL(0,23),W(1,1),W(1,2),GC_6,ZERO,ZERO
     $     ,PL(0,64),COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_0(WL(1,0,1,23),4,COEFS,4,4,WL(1,0
     $     ,1,64))
          CALL MP_VVVV4L2P0_1(PL(0,23),W(1,1),W(1,2),GC_6,ZERO,ZERO
     $     ,PL(0,65),COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_0(WL(1,0,1,23),4,COEFS,4,4,WL(1,0
     $     ,1,65))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,63),1,4,7,1,1,111,H)
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,64),1,4,7,1,1,112,H)
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,65),1,4,7,1,1,113,H)
C         Coefficient construction for loop diagram with ID 30
          CALL MP_VVV1L2P0_1(PL(0,56),W(1,2),GC_4,ZERO,ZERO,PL(0,66)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,56),4,COEFS,4,4,WL(1,0
     $     ,1,66))
          CALL MP_FFV1L3_2(PL(0,66),W(1,4),GC_5,MDL_MT,MDL_WT,PL(0,67)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_1(WL(1,0,1,66),4,COEFS,4,4,WL(1,0
     $     ,1,67))
          CALL MP_FFV1L1P0_3(PL(0,67),W(1,3),GC_5,ZERO,ZERO,PL(0,68)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_3_0(WL(1,0,1,67),4,COEFS,4,4,WL(1,0
     $     ,1,68))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,68),3,4,23,1,1,114
     $     ,H)
C         Coefficient construction for loop diagram with ID 31
          CALL MP_FFV1L3_1(PL(0,66),W(1,3),GC_5,MDL_MT,MDL_WT,PL(0,69)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_1(WL(1,0,1,66),4,COEFS,4,4,WL(1,0
     $     ,1,69))
          CALL MP_FFV1L2P0_3(PL(0,69),W(1,4),GC_5,ZERO,ZERO,PL(0,70)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_3_0(WL(1,0,1,69),4,COEFS,4,4,WL(1,0
     $     ,1,70))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,70),3,4,24,1,1,115
     $     ,H)
C         Coefficient construction for loop diagram with ID 32
          CALL MP_VVV1L2P0_1(PL(0,0),W(1,5),GC_4,ZERO,ZERO,PL(0,71)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,71))
          CALL MP_VVV1L2P0_1(PL(0,71),W(1,8),GC_4,ZERO,ZERO,PL(0,72)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,71),4,COEFS,4,4,WL(1,0
     $     ,1,72))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,72),2,4,1,2,1,116,H)
C         Coefficient construction for loop diagram with ID 33
          CALL MP_VVV1L2P0_1(PL(0,66),W(1,8),GC_4,ZERO,ZERO,PL(0,73)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_1(WL(1,0,1,66),4,COEFS,4,4,WL(1,0
     $     ,1,73))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,73),3,4,2,1,1,117,H)
C         Coefficient construction for loop diagram with ID 34
          CALL MP_VVVV1L2P0_1(PL(0,56),W(1,8),W(1,2),GC_6,ZERO,ZERO
     $     ,PL(0,74),COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_0(WL(1,0,1,56),4,COEFS,4,4,WL(1,0
     $     ,1,74))
          CALL MP_VVVV3L2P0_1(PL(0,56),W(1,8),W(1,2),GC_6,ZERO,ZERO
     $     ,PL(0,75),COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_0(WL(1,0,1,56),4,COEFS,4,4,WL(1,0
     $     ,1,75))
          CALL MP_VVVV4L2P0_1(PL(0,56),W(1,8),W(1,2),GC_6,ZERO,ZERO
     $     ,PL(0,76),COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_0(WL(1,0,1,56),4,COEFS,4,4,WL(1,0
     $     ,1,76))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,74),1,4,25,2,1,118
     $     ,H)
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,75),1,4,25,2,1,119
     $     ,H)
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,76),1,4,25,2,1,120
     $     ,H)
C         Coefficient construction for loop diagram with ID 35
          CALL MP_VVVV1L2P0_1(PL(0,30),W(1,8),W(1,1),GC_6,ZERO,ZERO
     $     ,PL(0,77),COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_0(WL(1,0,1,30),4,COEFS,4,4,WL(1,0
     $     ,1,77))
          CALL MP_VVVV3L2P0_1(PL(0,30),W(1,8),W(1,1),GC_6,ZERO,ZERO
     $     ,PL(0,78),COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_0(WL(1,0,1,30),4,COEFS,4,4,WL(1,0
     $     ,1,78))
          CALL MP_VVVV4L2P0_1(PL(0,30),W(1,8),W(1,1),GC_6,ZERO,ZERO
     $     ,PL(0,79),COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_0(WL(1,0,1,30),4,COEFS,4,4,WL(1,0
     $     ,1,79))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,77),1,4,26,2,1,121
     $     ,H)
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,78),1,4,26,2,1,122
     $     ,H)
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,79),1,4,26,2,1,123
     $     ,H)
C         Coefficient construction for loop diagram with ID 36
          CALL MP_VVVV1L2P0_1(PL(0,0),W(1,1),W(1,2),GC_6,ZERO,ZERO
     $     ,PL(0,80),COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_0(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,80))
          CALL MP_VVVV3L2P0_1(PL(0,0),W(1,1),W(1,2),GC_6,ZERO,ZERO
     $     ,PL(0,81),COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_0(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,81))
          CALL MP_VVVV4L2P0_1(PL(0,0),W(1,1),W(1,2),GC_6,ZERO,ZERO
     $     ,PL(0,82),COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_0(WL(1,0,1,0),4,COEFS,4,4,WL(1,0,1
     $     ,82))
          CALL MP_VVV1L2P0_1(PL(0,80),W(1,8),GC_4,ZERO,ZERO,PL(0,83)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,80),4,COEFS,4,4,WL(1,0
     $     ,1,83))
          CALL MP_VVV1L2P0_1(PL(0,81),W(1,8),GC_4,ZERO,ZERO,PL(0,84)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,81),4,COEFS,4,4,WL(1,0
     $     ,1,84))
          CALL MP_VVV1L2P0_1(PL(0,82),W(1,8),GC_4,ZERO,ZERO,PL(0,85)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,82),4,COEFS,4,4,WL(1,0
     $     ,1,85))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,83),1,4,1,2,1,124,H)
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,84),1,4,1,2,1,125,H)
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,85),1,4,1,2,1,126,H)
C         Coefficient construction for loop diagram with ID 37
          CALL MP_GHGHGL2_1(PL(0,0),W(1,5),GC_4,ZERO,ZERO,PL(0,86)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,0),1,COEFS,1,1,WL(1,0,1
     $     ,86))
          CALL MP_GHGHGL2_1(PL(0,86),W(1,8),GC_4,ZERO,ZERO,PL(0,87)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,86),1,COEFS,1,1,WL(1,0
     $     ,1,87))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,87),2,1,1,1,1,127,H)
C         Coefficient construction for loop diagram with ID 38
          CALL MP_GHGHGL1_2(PL(0,0),W(1,1),GC_4,ZERO,ZERO,PL(0,88)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,0),1,COEFS,1,1,WL(1,0,1
     $     ,88))
          CALL MP_GHGHGL1_2(PL(0,88),W(1,2),GC_4,ZERO,ZERO,PL(0,89)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,88),1,COEFS,1,1,WL(1,0
     $     ,1,89))
          CALL MP_GHGHGL1_2(PL(0,89),W(1,8),GC_4,ZERO,ZERO,PL(0,90)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_1(WL(1,0,1,89),1,COEFS,1,1,WL(1,0
     $     ,1,90))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,90),3,1,2,1,1,128,H)
C         Coefficient construction for loop diagram with ID 39
          CALL MP_GHGHGL2_1(PL(0,0),W(1,1),GC_4,ZERO,ZERO,PL(0,91)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_0_1(WL(1,0,1,0),1,COEFS,1,1,WL(1,0,1
     $     ,91))
          CALL MP_GHGHGL2_1(PL(0,91),W(1,2),GC_4,ZERO,ZERO,PL(0,92)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_1_1(WL(1,0,1,91),1,COEFS,1,1,WL(1,0
     $     ,1,92))
          CALL MP_GHGHGL2_1(PL(0,92),W(1,8),GC_4,ZERO,ZERO,PL(0,93)
     $     ,COEFS)
          CALL MP_ML5_0_UPDATE_WL_2_1(WL(1,0,1,92),1,COEFS,1,1,WL(1,0
     $     ,1,93))
          CALL MP_ML5_0_CREATE_LOOP_COEFS(WL(1,0,1,93),3,1,2,1,1,129,H)
 4000     CONTINUE
          MP_LOOP_REQ_SO_DONE=.TRUE.


C         Copy the qp wfs to the dp ones as they are used to setup the
C          CT calls.
C         This needs to be done once since only the momenta of these
C          WF matters.
          IF(.NOT.DPW_COPIED) THEN
            DO I=1,NWAVEFUNCS
              DO J=1,MAXLWFSIZE+4
                DPW(J,I)=DBLE(W(J,I))
              ENDDO
            ENDDO
            DPW_COPIED=.TRUE.
          ENDIF





        ENDIF
      ENDDO

      DO I=1,3
        DO J=0,NSQUAREDSO
          ANSDP(I,J)=ANS(I,J)
        ENDDO
      ENDDO

C     Grouping of loop diagrams now done directly when creating the
C      LOOPCOEFS.

      END
