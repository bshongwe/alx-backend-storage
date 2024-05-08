# 0x00. MySQL advanced 💻🧠
`Back-end` `SQL` `MySQL`

## Concepts to Explore 🔍
- Advanced SQL

## Resources 📚
- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.liquidweb.com/kb/mysql-optimization-how-to-leverage-mysql-database-indexing/)
- [Stored Procedure](https://www.w3resource.com/mysql/mysql-procedure.php)
- [Triggers](https://www.w3resource.com/mysql/mysql-triggers.php)
- [Views](https://www.w3resource.com/mysql/mysql-views.php)
- [Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/5.7/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/5.7/en/create-view.html)

## Learning Objectives 🎯
### General
- Explain how to create tables with constraints
- Optimize queries by adding indexes
- Implement stored procedures and functions in `MySQL`
- Implement views in `MySQL`
- Implement triggers in `MySQL`

## Requirements 📝
### General
- Execute files on `Ubuntu 18.04 LTS` using `MySQL` 5.7 (version 5.7.30)
- End files with a new line
- Add comments before `SQL` queries
- Start files with a comment describing the task
- Use uppercase for `SQL` keywords
- Include a `README.md` file at the `root` of the project folder
- Test file lengths using `wc`

## More Info ℹ️
- Comments for SQL files should be formatted as:
  ```
  $ cat my_script.sql
  -- Your SQL query here
  ```

# Tasks 📋
### Task 0. We are all unique! 🦄
**Description**: Create a table `users` with specified attributes
-	With these attributes:
	-	id, integer, never null, auto increment and primary key
	-	email, string (255 characters), never null and unique
	-	name, string (255 characters)
-	If the table already exists, your script should not fail
-	Your script can be executed on any database

<b>Context:</b> <i>Make an attribute unique directly in the table schema will enforced your business rules and avoid bugs in your application</i>
<br></br>

### Task 1. In and not out 💼
**Description**: Create a table `users` with additional attribute `country`
-	With these attributes:
	-	id, integer, never null, auto increment and primary key
	-	email, string (255 characters), never null and unique
	-	name, string (255 characters)
	-	country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)
-	If the table already exists, your script should not fail
-	Your script can be executed on any database
<br></br>

### Task 2. Best band ever! 🎸
- **Description**: Rank country origins of bands by number of fans
<br></br>

### Task 3. Old school band 🎶
- **Description**: List bands with Glam rock as their main style, ranked by longevity
<br></br>

### Task 4. Buy buy buy 💳
- **Description**: Create a trigger to decrease item quantity after adding a new order
<br></br>

### Task 5. Email validation to sent 📧
- **Description**: Create a trigger to reset `valid_email` attribute only when email has changed
<br></br>

### Task 6. Add bonus 🎉
- **Description**: Create a stored procedure `AddBonus` to add a new correction for a student
<br></br>

### 7. Average score 📊
- **Description**: Create a stored procedure `ComputeAverageScoreForUser` to compute and store the average score for a student
<br></br>


### 8. Optimize simple search 🔍
- **Description**: Create an index `idx_name_first` on the table `names` for the first letter of name
<br></br>


### 9. Optimize search and score 🔢
- **Description**: Create an index `idx_name_first_score` on the table `names` for the first letter of name and score
<br></br>


### 10. Safe divide 🛡️
- **Description**: Create a function `SafeDiv` to divide two numbers safely
<br></br>


### 11. No table for a meeting 🚫
- **Description**: Create a view `need_meeting` to list students with a score under 80 and no last meeting or more than 1 month
<br></br>


### 12. Average weighted score 📊
- **Description**: Create a stored procedure `ComputeAverageWeightedScoreForUser` that computes and stores the average weighted score for a student
<br></br>


### 13. Average weighted score for all! 📊
- **Description**: Create a stored procedure `ComputeAverageWeightedScoreForUsers` that computes and stores the average weighted score for all students
