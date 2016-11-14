

DROP DATABASE IF EXISTS `JobFinder`;

CREATE DATABASE IF NOT EXISTS `JobFinder`;

USE `JobFinder`;

CREATE TABLE IF NOT EXISTS `activityLog`(

	`activitytime` timestamp default now(),
	`activity` varchar(50)

);

CREATE TABLE IF NOT EXISTS `USER`(
	`Userid` int(5) AUTO_INCREMENT,
	`Username` varchar(25),
	`Password` varchar(41),
	
	UNIQUE (Username),
	constraint USER_Userid_pk primary key(Userid)
);


CREATE TABLE IF NOT EXISTS `JOBSEEKER`(
	`Userid` int(5) AUTO_INCREMENT,
	`Age` int(2),
	
	FOREIGN KEY(Userid) REFERENCES USER(Userid)
);

CREATE TABLE IF NOT EXISTS `COMPANY`(
	`Companyid` int(5) AUTO_INCREMENT,
	`Details` varchar(25),
	`Companyname` varchar(41),
	
	PRIMARY KEY(Companyid)
);

CREATE TABLE IF NOT EXISTS `COMPANYREP`(
	`Userid` int(5) AUTO_INCREMENT,
	`Priviledge` int(2),
	`Companyid` int(5),
	
	FOREIGN KEY(Userid) REFERENCES USER(Userid),
	FOREIGN KEY(Companyid) REFERENCES COMPANY(Companyid)
);


CREATE TABLE IF NOT EXISTS `JOB`(
	
	`Jobid` int(5) AUTO_INCREMENT,
	`Industry` varchar(50),
	`Jobtitle` varchar(50),
	`Agerequirement` int(2),
	`Level` varchar(25),
	`Salary` varchar(50),
	`Dateposted` datetime default current_timestamp on update current_timestamp,
	`Enddate` datetime default current_timestamp on update current_timestamp,
	`Status` varchar(10),
	`Userid` int(5),
	
	PRIMARY KEY(Jobid),
	FOREIGN KEY(Userid) REFERENCES USER(Userid)

);


CREATE TABLE IF NOT EXISTS `USERCONTACTNUMBER`(

	`Userid` int(5),
	`ContactNumber` varchar(16),
	
	primary key(ContactNumber),
	FOREIGN KEY (Userid) REFERENCES USER(Userid)
);

CREATE TABLE IF NOT EXISTS `USEREMAILADDRESS`(

	`Userid` int(5),
	`Emailaddress` varchar(31),
	
	primary key(Emailaddress),
	FOREIGN KEY (Userid) REFERENCES USER(Userid)
);

CREATE TABLE IF NOT EXISTS `APPLIES`(

	`Userid` int(5),
	`Jobid` int(5),
	`Dateapplied` varchar(16),
	
	FOREIGN KEY (Userid) REFERENCES USER(Userid),
	FOREIGN KEY(Jobid) REFERENCES JOB(Jobid)
);

CREATE TABLE IF NOT EXISTS `JOBSEEKERSKILLSET`(

	`Userid` int(5),
	`Skillset` varchar(16),
	
	FOREIGN KEY (Userid) REFERENCES JOBSEEKER(Userid)
);

CREATE TABLE IF NOT EXISTS `JOBSEEKERADDRESS`(

	`Userid` int(5),
	`Address` varchar(16),
	
	FOREIGN KEY (Userid) REFERENCES JOBSEEKER(Userid)
);

CREATE TABLE IF NOT EXISTS `COMPANYADDRESS`(

	`Companyid` int(5),
	`Address` varchar(16),
	
	FOREIGN KEY (Companyid) REFERENCES COMPANY(Companyid)
);

CREATE TABLE IF NOT EXISTS `JSEDUCATIONALATTAINMENT`(

	`Userid` int(5),
	`EducationalAttainment` varchar(16),
	
	FOREIGN KEY (Userid) REFERENCES JOBSEEKER(Userid)
);

CREATE TABLE IF NOT EXISTS `JOBSKILLSETREQ`(

	`Jobid` int(5),
	`Skillsetreq` varchar(16),
	
	FOREIGN KEY (Jobid) REFERENCES JOB(Jobid)
);


DELIMITER %%

	CREATE trigger userInsertLog after insert on `USER`
		 for each row
		 	begin
		 	insert into activityLog(activity) values('Inserted new User');
		 	
		 	end;
%%
	CREATE trigger userDeleteLog after delete on `USER`
		 for each row
		 	begin
		 	insert into activityLog(activity) values('Deleted a User');
		 	
		 	end;
%%
	CREATE trigger userUpdateLog after update on `USER`
		 for each row
		 	begin
		 	insert into activityLog(activity) values('Updated a User');
		 	
		 	end;
%%
	CREATE trigger jobInsertLog after insert on `JOB`
		 for each row
		 	begin
		 	insert into activityLog(activity) values('Inserted new Job');
		 	
		 	end;
%%		
	CREATE trigger jobDeleteLog after delete on `JOB`
		 for each row
		 	begin
		 	insert into activityLog(activity) values('Deleted a Job');
		 	
		 	end;
%%
	CREATE trigger jobUpdateLog after update on `JOB`
		 for each row
		 	begin
		 	insert into activityLog(activity) values('Updated a Job');
		 	end;
		 	
%% 
	CREATE trigger companyInsertLog after insert on `COMPANY`
		 for each row
		 	begin
		 	insert into activityLog(activity) values('Inserted new Company');
		 	
		 	end;
%%
	CREATE trigger companyDeleteLog after delete on `COMPANY`
		 for each row
		 	begin
		 	insert into activityLog(activity) values('Deleted a Company');
		 	
		 	end;
%%
	CREATE trigger companyUpdateLog after update on `COMPANY`
		 for each row
		 	begin
		 	insert into activityLog(activity) values('Updated a Company');
		 	end;
%%
		
DELIMITER ;





