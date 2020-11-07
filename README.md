# ItSkillExtractor

Extract IT skills from text

Example:
1. Extract from string 
```
extract_skill('Git  C#  MS SQL Server  Developer Express  Java  JavaScript  Unit Testing  Android  MongoDB  RabbitMQ  Spring Framework')
>> ['c#', 'express', 'rabbitmq', 'sql_server', 'mongodb', 'git', 'mssql', 'javascript', 'android', 'java', 'spring_framework_beans', 'developer', 'unit_testing']
```
2. Extract from string
```
extract_skill('Стек технологий: java, spring framework.')
>> ['java', 'spring_framework_beans']

```
