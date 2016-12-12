DROP  USER "project127"@"localhost";

CREATE USER "project127"@"localhost" identified by "password";

GRANT ALL PRIVILEGES ON JobFinder.* to "project127"@"localhost";

DROP DATABASE IF EXISTS `JobFinder`;

CREATE DATABASE IF NOT EXISTS `JobFinder`;

USE `JobFinder`;

CREATE TABLE IF NOT EXISTS `activityLog`(

	`activitytime` timestamp default now(),
	`activity` text,
	`OldValue` text DEFAULT NULL,
	`NewValue` text DEFAULT NULL
);


CREATE TABLE IF NOT EXISTS `USERS`(
	`Userid` int(5) AUTO_INCREMENT,
	`Username` varchar(25),
	`Password` varchar(33),
	`Name` varchar(40),
	
	UNIQUE (Username),
	constraint USER_Userid_pk primary key(Userid)
);


CREATE TABLE IF NOT EXISTS `JOBSEEKER`(
	`Userid` int(5),
	`Age` int(2),
	
	FOREIGN KEY(Userid) REFERENCES USERS(Userid) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS `COMPANY`(
	`Companyid` int(5) AUTO_INCREMENT,
	`Companyname` varchar(41),
	`Details` varchar(25),
	
	PRIMARY KEY(Companyid)
);

CREATE TABLE IF NOT EXISTS `COMPANYREP`(
	`Userid` int(5),
	`Privilege` varchar(100),
	`Companyid` int(5) default NULL,
	`Companyname` varchar(41),

	FOREIGN KEY(Userid) REFERENCES USERS(Userid) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY(Companyid) REFERENCES COMPANY(Companyid) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS `JOB`(
	
	`Jobid` int(5) AUTO_INCREMENT,
	`Industry` varchar(50),
	`Jobtitle` varchar(50),
	`Agerequirement` int(2),
	`JLevel` varchar(25),
	`Salary` varchar(50),
	`Dateposted` datetime default current_timestamp on update current_timestamp,
	`Enddate` datetime,
	`Status` varchar(10),
	`Userid` int(5),
	
	PRIMARY KEY(Jobid),
	FOREIGN KEY(Userid) REFERENCES USERS(Userid) ON DELETE CASCADE ON UPDATE CASCADE

);


CREATE TABLE IF NOT EXISTS `USERCONTACTNUMBER`(

	`Userid` int(5),
	`ContactNumber` varchar(16),
	
	FOREIGN KEY (Userid) REFERENCES USERS(Userid) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS `USEREMAILADDRESS`(

	`Userid` int(5),
	`Emailaddress` varchar(31),
	
	FOREIGN KEY (Userid) REFERENCES USERS(Userid) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS `APPLIES`(

	`Userid` int(5),
	`Jobid` int(5),
	`Dateapplied` datetime default current_timestamp on update current_timestamp,
	
	FOREIGN KEY (Userid) REFERENCES USERS(Userid) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY(Jobid) REFERENCES JOB(Jobid) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS `JOBSEEKERSKILLSET`(

	`Userid` int(5),
	`Skillset` varchar(16),
	
	FOREIGN KEY (Userid) REFERENCES USERS(Userid) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS `JOBSEEKERADDRESS`(

	`Userid` int(5),
	`Address` varchar(100),
	
	FOREIGN KEY (Userid) REFERENCES USERS(Userid) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS `COMPANYADDRESS`(

	`Companyid` int(5),
	`Address` varchar(100),
	
	FOREIGN KEY (Companyid) REFERENCES COMPANY(Companyid) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS `JSEDUCATIONALATTAINMENT`(

	`Userid` int(5),
	`EducationalAttainment` varchar(50),
	
	FOREIGN KEY (Userid) REFERENCES USERS(Userid) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS `JOBSKILLSETREQ`(

	`Jobid` int(5),
	`Skillsetreq` varchar(50),	
	
	FOREIGN KEY (Jobid) REFERENCES JOB(Jobid) ON DELETE CASCADE ON UPDATE CASCADE
);


DELIMITER %%
	CREATE TRIGGER userInsert AFTER INSERT ON USERS
		FOR EACH ROW
			BEGIN
				INSERT INTO activityLog(activity, NewValue) VALUES("Inserted New User", NEW.Username);
			END;
			
%%

	CREATE TRIGGER userDelete AFTER DELETE ON USERS
		FOR EACH ROW
			BEGIN
				INSERT INTO activityLog(activity, OldValue) VALUES("Deleted a User", OLD.Username);
			END;
			
%%
	CREATE TRIGGER jobInsert AFTER INSERT ON JOB
		FOR EACH ROW
			BEGIN
				INSERT INTO activityLog(activity, NewValue) VALUES("Created New Job", NEW.Jobtitle);
			END;
%%
	CREATE TRIGGER jobDelete AFTER DELETE ON JOB
		FOR EACH ROW
			BEGIN
				INSERT INTO activityLog(activity, OldValue) VALUES("Deleted a Job", OLD.Jobtitle);
			END;
%%
	CREATE TRIGGER companyInsert AFTER INSERT ON COMPANY
		FOR EACH ROW 
			BEGIN
				INSERT INTO activityLog(activity, NewValue) VALUES("Inserted New Company", NEW.Companyname);
			END;
%%
	CREATE TRIGGER companyDelete AFTER DELETE ON COMPANY
		FOR EACH ROW
			BEGIN
				INSERT INTO activityLog(activity, OldValue) VALUES("Deleted a Company", OLD.Companyname);
			END;
%%
	CREATE PROCEDURE userInsertLog(in uname varchar(25), in pword varchar(41), in userName varchar(40))
		BEGIN
			INSERT INTO USERS(Username, Password, Name) VALUES(uname, md5(pword), userName);
		END;
		
%%
	
	CREATE PROCEDURE AddEmail(in jsEmailAd varchar(31))
		BEGIN
		
			INSERT INTO USEREMAILADDRESS(Userid, Emailaddress) VALUES((select Userid from USERS where Userid = LAST_INSERT_ID()), jsEmailAd);
		
		END;

%%
	CREATE PROCEDURE AddEmailId(in Usid int(5), in jsEmailAd varchar(31))
		BEGIN
			INSERT INTO USEREMAILADDRESS(Userid, Emailaddress) VALUES(Usid, jsEmailAd);
		END;
%%

	CREATE PROCEDURE AddCNumber(in jsContactnumber varchar(16))
		BEGIN
		
			INSERT INTO USERCONTACTNUMBER(Userid, ContactNumber) VALUES((select Userid from USERS where Userid = LAST_INSERT_ID()), jsContactnumber);
			
		END;

%%
	CREATE PROCEDURE AddCNumberId(in Usid int(5), in jsContactnumber varchar(16))
		BEGIN
			INSERT INTO USERCONTACTNUMBER(Userid, ContactNumber) VALUES(Usid, jsContactnumber);
		END;
%%

	CREATE PROCEDURE updateUser(in Usid int(5), in uname varchar(25), in pword varchar(41), name varchar(40))
		BEGIN
			INSERT INTO activityLog(activity, OldValue, NewValue) VALUES(concat("Updated User: ", uname),concat((select Username from USERS where Userid = Usid), "-", (select Password from USERS where Userid = Usid), "-", (select Name from USERS where Userid = Usid)),concat(uname, "-", md5(pword), "-",name));
			
			UPDATE USERS SET Username = uname, Password = md5(pword), Name = name where Userid = Usid;
		END;

%%


	CREATE PROCEDURE jsInsertLog(in jsAge int(2))
		BEGIN	
			INSERT INTO JOBSEEKER(Userid, Age) VALUES((select Userid from USERS where Userid = LAST_INSERT_ID()), jsAge);
		END;
		
%% 
	
	CREATE PROCEDURE jsAddAddress(in jsAddress varchar(100))
		BEGIN
			INSERT INTO JOBSEEKERADDRESS(Userid, Address) VALUES((select Userid from USERS where Userid = LAST_INSERT_ID()), jsAddress);
		END;
%%

	CREATE PROCEDURE jsAddAddressId(in Usid int(5), in jsAddress varchar(100))
		BEGIN
			INSERT INTO JOBSEEKERADDRESS(Userid, Address) VALUES(Usid, jsAddress);
		END;
%%
	

	CREATE PROCEDURE jsAddSkillSet(in jsSkillset varchar(16))
		BEGIN
		
			INSERT INTO JOBSEEKERSKILLSET(Userid, Skillset) VALUES((select Userid from USERS where Userid = LAST_INSERT_ID()), jsSkillset);
	
		END;
		
%%
	CREATE PROCEDURE jsAddSkillSetId(in Usid int(5), in jsSkillset varchar(16))
		BEGIN
		
			INSERT INTO JOBSEEKERSKILLSET(Userid, Skillset) VALUES(Usid, jsSkillset);
	
		END;
		
%%
	CREATE PROCEDURE jsAddEduc(in jsEducAtt varchar(50))
		BEGIN
		INSERT INTO JSEDUCATIONALATTAINMENT(Userid, EducationalAttainment) VALUES((select Userid from USERS where Userid = LAST_INSERT_ID()), jsEducAtt);
		END;

%%
	CREATE PROCEDURE jsAddEducId(in Usid int(5), in jsEducAtt varchar(50))
		BEGIN
		INSERT INTO JSEDUCATIONALATTAINMENT(Userid, EducationalAttainment) VALUES(Usid, jsEducAtt);
		END;

%%
	CREATE PROCEDURE deleteUser(in Usid int(5))
	BEGIN
		
		DELETE FROM USERCONTACTNUMBER where Userid = Usid;
		DELETE FROM USEREMAILADDRESS where Userid = Usid;
		DELETE FROM USERS where Userid = Usid;
	END;
%%
	CREATE PROCEDURE jsDeleteLog(in Usid int(5))
		BEGIN
			
			DELETE FROM JOBSEEKER where Userid = Usid;
			DELETE FROM JOBSEEKERSKILLSET where Userid = Usid;
			DELETE FROM JOBSEEKERADDRESS where Userid = Usid;
			DELETE FROM JSEDUCATIONALATTAINMENT where Userid = Usid;
		END;
		
%%
	CREATE PROCEDURE jsUpdateAge(in Usid int(5), in jsAge int(2))
		BEGIN
			INSERT INTO activityLog(activity, OldValue, NewValue) VALUES(concat("Updated User ", jsAge, "  - Age"),(select Age From JOBSEEKER where Userid = Usid), jsAge);
			
			UPDATE JOBSEEKER SET Age = jsAge where Userid = Usid;
		END;
	
%%
	
	CREATE PROCEDURE cInsertLog(in cPrivilege varchar(100), in cCompanyname varchar(41))
		BEGIN
			INSERT INTO COMPANYREP(Userid, Privilege, Companyid, Companyname) VALUES((select Userid from USERS where Userid = LAST_INSERT_ID()), cPrivilege, (select Companyid from COMPANY where Companyname = cCompanyname LIMIT 1), cCompanyname);
			
		END;
%%


	CREATE PROCEDURE cDeleteLog(in Usid int(5))
		BEGIN
			DELETE FROM COMPANYREP where Userid =Usid;
		END;
		
%%

	CREATE PROCEDURE cUpdateLog(in Usid int(5), in cPrivilege varchar(100), in cCompanyname varchar(41))
		BEGIN
			INSERT INTO activityLog(activity, OldValue, NewValue) VALUES(concat("Updated Company Representative: ", (select Username from USERS where Userid = Usid)), concat((select Privilege from COMPANYREP where Userid = Usid), "-", (select CompanyName from COMPANYREP where Userid = Usid)), concat(cPrivilege, "-",cCompanyname));
			
			UPDATE COMPANYREP SET Privilege = cPrivilege, Companyid = (select Companyid from COMPANY where Companyname = cCompanyname LIMIT 1), Companyname = cCompanyname where Userid = Usid;
		END;

%%

	CREATE PROCEDURE jobInsertLog(in ind varchar(50), in jTitle varchar(50), in areq int(2), in lev varchar(20), in sal varchar(50), in edate datetime, in status varchar(10), in userid int(5))
		BEGIN
			INSERT INTO JOB(Industry, Jobtitle, Agerequirement, JLevel, Salary, Enddate, Status, Userid) VALUES(ind, jTitle, areq, lev, sal, edate, status, userid);
			
		END;
		
%%
	CREATE PROCEDURE jobAddSkillSet(in job_id int(5), in jobSkillReq varchar(50))
		BEGIN
			INSERT INTO JOBSKILLSETREQ(Jobid, Skillsetreq) VALUES(job_id, jobSkillReq);
		END;	
%%
	
	CREATE PROCEDURE jobDeleteLog(in job_id int(5))
		BEGIN
			DELETE FROM JOB where Jobid = job_id;
			DELETE FROM JOBSKILLSETREQ WHERE Jobid = job_id;
		END;
		
%%

	CREATE PROCEDURE jobUpdateLog(in job_id int(5), in ind varchar(50), in jTitle varchar(50), in areq int(2), in lev varchar(20), in sal varchar(50), in edate datetime, in status varchar(10))
		BEGIN
			INSERT INTO activityLog(activity, OldValue, NewValue) VALUES(concat("Updated Job Requirements of: ", (select Jobtitle from JOB where Jobid = job_id)), concat((select Industry from JOB where Jobid = job_id), "-", (select Jobtitle from JOB where Jobid = job_id), "-",(select Agerequirement from JOB where Jobid = job_id), "-",(select JLevel from JOB where Jobid = job_id), "-",(select Salary from JOB where Jobid = job_id), "-",(select Enddate from JOB where Jobid = job_id), "-",(select Status from JOB where Jobid = job_id)),concat(ind , "-", jTitle, "-",areq, "-",lev, "-",sal, "-",edate, "-",status));
			
			UPDATE JOB SET Industry = ind, Jobtitle = jTitle, Agerequirement = areq, JOB.JLevel = lev, Salary = sal, Enddate = edate, Status = status where JOB.Jobid = job_id;
		END;
		
%%
	CREATE PROCEDURE companyInsertLog(in cname varchar(41), in dtails varchar(25))
		BEGIN
			INSERT INTO COMPANY(Companyname, Details) VALUES(cname, dtails);
		END;
		
%%
	CREATE PROCEDURE compAddAddress(in compAddress varchar(100))
		BEGIN
			INSERT INTO COMPANYADDRESS(Companyid, Address) VALUES((select Companyid from COMPANY where Companyid = LAST_INSERT_ID()), compAddress);
		END;
%%
	CREATE PROCEDURE compAddAddressId(in cid int(5), in compAddress varchar(100))
		BEGIN
			INSERT INTO COMPANYADDRESS(Companyid, Address) VALUES(cid, compAddress);
		END;
%%

	CREATE PROCEDURE companyDeleteLog(in cid int(5))
		BEGIN
			DELETE FROM COMPANY where Companyid = cid;
			DELETE FROM COMPANYADDRESS WHERE Companyid = cid;
		END;
		
%%

	CREATE PROCEDURE companyUpdateLog(in cid int(5), in cname varchar(41), in dtails varchar(25), in compAddress varchar(100))
		BEGIN
			INSERT INTO activityLog(activity, OldValue, NewValue) VALUES(concat("Updated Company: ", cname), concat((select Companyname from COMPANY where Companyid = cid), "-",(select Details from COMPANY where Companyid = cid)), concat( cname, "-",dtails));
			
			UPDATE COMPANY SET Companyname = cname, Details = dtails where Companyid = cid;
		END;

%%

	CREATE PROCEDURE apply (in Usid int(5), in job_id int(5))
		BEGIN
			INSERT INTO activityLog(activity) VALUES(concat(Usid, " applied for ", job_id));
		
			INSERT INTO APPLIES(Userid, Jobid) VALUES(Usid, job_id);
		END;
%%
	CREATE PROCEDURE jsPrint(in jsId int(5))
		BEGIN
			SELECT A.Userid, A.Username, A.Password, A.Name, B.ContactNumber, C.Emailaddress, JSA.Address, JSSS.Skillset, JSEA.EducationalAttainment From USERS AS A JOIN USERCONTACTNUMBER AS B JOIN USEREMAILADDRESS AS C JOIN JOBSEEKERADDRESS AS JSA JOIN JOBSEEKERSKILLSET AS JSSS JOIN JSEDUCATIONALATTAINMENT AS JSEA ON (A.Userid = jsId) and A.Userid = B.Userid and (A.Userid = C.Userid) and A.Userid = JSA.Userid and A.Userid = JSSS.Userid and A.Userid = JSEA.Userid;
		END;	
%%
	CREATE PROCEDURE jsPrintAll()
		BEGIN
			SELECT A.Userid, A.Username, A.Password, A.Name, B.ContactNumber, C.Emailaddress, JSA.Address, JSSS.Skillset, JSEA.EducationalAttainment From USERS AS A JOIN USERCONTACTNUMBER AS B JOIN USEREMAILADDRESS AS C JOIN JOBSEEKERADDRESS AS JSA JOIN JOBSEEKERSKILLSET AS JSSS JOIN JSEDUCATIONALATTAINMENT AS JSEA ON (A.Userid = B.Userid) and (A.Userid = C.Userid) and (A.Userid = JSA.Userid) and (A.Userid = JSSS.Userid) and (A.Userid = JSEA.Userid);
		END;
		
%%
	CREATE PROCEDURE compRepPrint(in cid int(5))
		BEGIN
			SELECT A.Userid, A.Username, A.Password, A.Name, B.ContactNumber, C.Emailaddress, CREP.Privilege, CREP.Companyid, CREP.Companyname From USERS AS A JOIN USERCONTACTNUMBER AS B JOIN USEREMAILADDRESS AS C JOIN COMPANYREP AS CREP ON (A.Userid = cid) and A.Userid = B.Userid and (A.Userid = C.Userid) and A.Userid = CREP.Userid;
		END;
		
%%
	CREATE PROCEDURE compRepPrintAll()
		BEGIN
			SELECT A.Userid, A.Username, A.Password, A.Name, B.ContactNumber, C.Emailaddress, CREP.Privilege, CREP.Companyid, CREP.Companyname From USERS AS A JOIN USERCONTACTNUMBER AS B JOIN USEREMAILADDRESS AS C JOIN COMPANYREP AS CREP ON A.Userid = B.Userid and (A.Userid = C.Userid) and A.Userid = CREP.Userid;
		END;
		
%%
	CREATE PROCEDURE cPrint(in compId int(5))
		BEGIN
			SELECT A.Companyid, A.Companyname, A.Details, B.Address FROM COMPANY AS A JOIN COMPANYADDRESS AS B ON (A.Companyid = compId) and A.Companyid = B.Companyid;
		
		END;
%%		
	CREATE PROCEDURE cPrintAll()
		BEGIN
			SELECT A.Companyid, A.Companyname, A.Details, B.Address FROM COMPANY AS A JOIN COMPANYADDRESS AS B ON A.Companyid = B.Companyid;

		END;
%%

DELIMITER ;
