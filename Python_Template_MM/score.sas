options validvarname=upcase;
%let WORK_DIR = D:\AlfaPythonToMM\pywd;
%let PYTHON_PATH = C:\ProgramData\Anaconda3\python.exe;

%put SCORING_PYTHON;

libname worklib "&WORK_DIR\pydump";

%macro utl_submit_py64(pgm_path);
  %if %symexist(SCOREFILESDIR) = 0 %then %do;
    /* Scoring from score task, need to download model files first */
    data _null_;
        infile FDisp; /* From scoring task, Pre-code */
        input;
        file "&WORK_DIR\pydump\field_disp.dat" lrecl=4096;
        put _infile_;
    run;
    
    data _null_;
        infile Model; /* From scoring task, Pre-code */
        input;
        file "&WORK_DIR\pydump\model.dat" lrecl=4096;
        put _infile_;
    run;
    
    %let SCOREFILESDIR = &WORK_DIR\pydump;
  %end;
  filename rut pipe "&PYTHON_PATH "&pgm_path" ""&SCOREFILESDIR"" ""&WORK_DIR\pydump""";
  data _null_;
    file print;
    infile rut;
    input;
    put _infile_;
  run;
  filename rut clear;
%mend utl_submit_py64;

data worklib.score;
   set &_MM_InputDS;
run;

%utl_submit_py64("&WORK_DIR\score.py");

proc import out=predict datafile="&WORK_DIR.\pydump\predict.csv" dbms=csv replace;
run;

data &_MM_OutputDS;
    set &_MM_InputDS;
    set predict;
run;
