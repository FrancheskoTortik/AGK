region_dick = {}

with open('reg.txt', 'r', encoding='UTF-8') as file:
    for i in file.readlines():
        region_dick[int(i.split()[0])] = i.split()[1]
        #print(i.split()[1])
print(region_dick)

agk = """17	Абинский район-
19	Абинский район-
27	Анапа-
25	Анапа-
26	Анапа-
28	Анапа-
113	Апшеронский район-
114	Апшеронский район-
115	Апшеронский район-
4	Армавир-
31	Белореченский район-
30	Белореченский район-
50	Белореченский район-
32	Белореченский район-
51	Белореченский район-
105	Брюховеций район-
106	Брюховеций район-
107	Брюховеций район-
111	Брюховеций район-
108	Брюховеций район-
69	Геленджик-
62	Геленджик-
63	Геленджик-
64	Геленджик-
65	Геленджик-
66	Геленджик-
70	Геленджик-
71	Геленджик-
72	Геленджик-
67	Геленджик-
73	Геленджик-
74	Геленджик-
68	Геленджик-
75	Геленджик-
76	Геленджик-
77	Геленджик-
78	Геленджик-
79	Геленджик-
87	Горячий глюч-
88	Горячий глюч-
42	Гулькевичский район-
116	Ейскиий район-
117	Ейскиий район-
118	Ейскиий район-
119	Ейскиий район-
43	Кавказский район-
109	Калининский район
112	Калининский район
29	Краснодар-
10	Крымский район-
9	Крымский район-
5	Крымский район-
14	Крымский район-
8	Крымский район-
6	Крымский район-
16	Крымский район-
7	Крымский район-
11	Крымский район-
13	Крымский район-
126	Крымский район-
61	Крымский район-
131	Курганинский район-
132	Курганинский район-
133	Курганинский район-
120	Лабинский район-
121	Лабинский район-
124	Лабинский район-
127	Лабинский район-
122	Лабинский район-
128	Лабинский район-
129	Лабинский район-
130	Лабинский район-
123	Лабинский район-
12	Лабинский район-
125	Лабинский район-
33	Мостовской район-
39	Мостовской район-
35	Мостовской район-
44	Мостовской район-
46	Мостовской район-
36	Мостовской район-
138	Мостовской район-
139	Мостовской район-
52	Мостовской район-
53	Мостовской район-
80	Мостовской район-
82	Мостовской район-
83	Мостовской район-
81	Мостовской район-
84	Мостовской район-
134	Новокубанский район-
135	Новокубанский район-
45	Новокубанский район-
136	Новокубанский район-
47	Новороссийск-
57	Новороссийск-
58	Новороссийск-
48	Новороссийск-
49	Новороссийск-
54	Новороссийск-
55	Новороссийск-
56	Новороссийск-
59	Новороссийск-
60	Новороссийск-
97	Отрадненский
98	Отрадненский
99	Отрадненский
100	Отрадненский
101	Отрадненский
102	Отрадненский
103	Приморско-Ахтарский район-
110	Приморско-Ахтарский район-
104	Приморско-Ахтарский район-
15	Северский район-
2	Северский район-
20	Северский район-
22	Северский район-
21	Славянский район-
18	Славянский район-
149	Сочи-
150	Сочи-
151	Сочи-
152	Сочи-
153	Сочи-
37	Сочи-
38	Сочи-
154	Сочи-
155	Сочи-
156	Сочи-
157	Сочи-
158	Сочи-
159	Сочи-
89	Сочи-
90	Сочи-
160	Сочи-
161	Сочи-
162	Сочи-
163	Сочи-
165	Сочи-
166	Сочи-
167	Сочи-
168	Сочи-
169	Сочи-
170	Сочи-
171	Сочи-
172	Сочи-
173	Сочи-
174	Сочи-
175	Сочи-
176	Сочи-
177	Сочи-
178	Сочи-
179	Сочи-
180	Сочи-
181	Сочи-
182	Сочи-
183	Сочи-
184	Сочи-
185	Сочи-
186	Сочи-
187	Сочи-
188	Сочи-
189	Сочи-
190	Сочи-
191	Сочи-
192	Сочи-
193	Сочи-
111	Сочи-
86	Тбилисский район-
24	Темрюкский район-
23	Темрюкский район-
40	Туапсинский район-
34	Туапсинский район-
140	Туапсинский район-
141	Туапсинский район-
91	Туапсинский район-
95	Туапсинский район-
96	Туапсинский район-
142	Туапсинский район-
143	Туапсинский район-
144	Туапсинский район-
92	Туапсинский район-
93	Туапсинский район-
94	Туапсинский район-
145	Туапсинский район-
146	Туапсинский район-
147	Туапсинский район-
148	Туапсинский район-
137	Успенский район-
41	Усть-Лабинский район-
85	Усть-Лабинский район-
"""