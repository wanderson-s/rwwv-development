INSERT INTO public.employees (email, password, first_name, last_name, birth_date, position, first_access, active, can_simulate_budget, can_submit_budget, can_approve_budget, can_read_budget, is_admin, created_at, updated_at) VALUES ('carlos.rian@taimin.com.br', 'cc0df3eb0ae105e79ae822b83d2cd20f', 'Zack', 'Bedbury', '1972-09-20', 'director', true, true, true, false, true, true, true, '2021-08-31 11:27:01.413131', '2021-08-31 11:27:01.413131');
INSERT INTO public.employees (email, password, first_name, last_name, birth_date, position, first_access, active, can_simulate_budget, can_submit_budget, can_approve_budget, can_read_budget, is_admin, created_at, updated_at) VALUES ('zack.bedbury@taimin.com.br', 'cc0df3eb0ae105e79ae822b83d2cd20f', 'Zack', 'Bedbury', '1972-09-20', 'director', false, true, true, false, true, true, false, '2021-08-31 11:27:01.413131', '2021-08-31 11:27:01.413131');
INSERT INTO public.employees (email, password, first_name, last_name, birth_date, position, first_access, active, can_simulate_budget, can_submit_budget, can_approve_budget, can_read_budget, is_admin, created_at, updated_at) VALUES ('zarah.hulks@taimin.com.br', 'cc0df3eb0ae105e79ae822b83d2cd20f', 'Zarah', 'Hulks', '1971-05-06', 'analyst', false, true, true, true, false, true, false, '2021-08-31 11:27:01.413166', '2021-08-31 11:27:01.413166');
INSERT INTO public.employees (email, password, first_name, last_name, birth_date, position, first_access, active, can_simulate_budget, can_submit_budget, can_approve_budget, can_read_budget, is_admin, created_at, updated_at) VALUES ('zacharie.nassy@taimin.com.br', 'cc0df3eb0ae105e79ae822b83d2cd20f', 'Zacharie', 'Nassy', '1987-12-11', 'analyst', false, true, true, true, false, true, false, '2021-08-31 11:27:01.412953', '2021-08-31 11:27:01.412953');
INSERT INTO public.employees (email, password, first_name, last_name, birth_date, position, first_access, active, can_simulate_budget, can_submit_budget, can_approve_budget, can_read_budget, is_admin, created_at, updated_at) VALUES ('zacharie.reddington@taimin.com.br', 'cc0df3eb0ae105e79ae822b83d2cd20f', 'Zacharie', 'Reddington', '1979-03-30', 'analyst', false, true, true, true, false, true, false, '2021-08-31 11:27:01.412943', '2021-08-31 11:27:01.412943');
INSERT INTO public.employees (email, password, first_name, last_name, birth_date, position, first_access, active, can_simulate_budget, can_submit_budget, can_approve_budget, can_read_budget, is_admin, created_at, updated_at) VALUES ('pavel.heather@taimin.com.br', 'cc0df3eb0ae105e79ae822b83d2cd20f', 'Pavel', 'Heather', '1983-08-14', 'manager', false, true, true, true, false, true, false, '2021-08-31 11:27:01.412892', '2021-08-31 11:27:01.412892');
INSERT INTO public.employees (email, password, first_name, last_name, birth_date, position, first_access, active, can_simulate_budget, can_submit_budget, can_approve_budget, can_read_budget, is_admin, created_at, updated_at) VALUES ('pepe.leverington@taimin.com.br', 'cc0df3eb0ae105e79ae822b83d2cd20f', 'Pepe', 'Leverington', '1996-01-06', 'manager', false, true, true, true, true, true, false, '2021-08-31 11:27:01.413207', '2021-08-31 11:27:01.413207');INSERT INTO public.budget (name, created_at, updated_at, fk_id_employees) VALUES ('GA 01 BUDGET 1', '2021-09-04 21:30:50.486920', '2021-09-04 21:30:50.486997', 1);
INSERT INTO public.budget (name, created_at, updated_at, fk_id_employees) VALUES ('GA 01 BUDGET 3', '2021-09-04 21:31:07.028080', '2021-09-04 21:31:07.028103', 1);
INSERT INTO public.budget (name, created_at, updated_at, fk_id_employees) VALUES ('GA 01 BUDGET 4', '2021-09-04 21:31:11.047392', '2021-09-04 21:31:11.047415', 1);
INSERT INTO public.budget (name, created_at, updated_at, fk_id_employees) VALUES ('GA 01 BUDGET 5', '2021-09-04 21:31:15.061421', '2021-09-04 21:31:15.061449', 1);
INSERT INTO public.budget (name, created_at, updated_at, fk_id_employees) VALUES ('GA 01 BUDGET 6', '2021-09-04 21:31:19.501610', '2021-09-04 21:31:19.501634', 1);
INSERT INTO public.budget (name, created_at, updated_at, fk_id_employees) VALUES ('GA 01 BUDGET 7', '2021-09-04 21:31:23.352882', '2021-09-04 21:31:23.352913', 1);
INSERT INTO public.budget (name, created_at, updated_at, fk_id_employees) VALUES ('GA 01 BUDGET 8', '2021-09-04 21:31:26.964987', '2021-09-04 21:31:26.965012', 1);
INSERT INTO public.budget (name, created_at, updated_at, fk_id_employees) VALUES ('GA 01 BUDGET 9', '2021-09-04 21:31:31.311704', '2021-09-04 21:31:31.311742', 1);
INSERT INTO public.budget (name, created_at, updated_at, fk_id_employees) VALUES ('GA 01 BUDGET 10', '2021-09-04 21:31:36.186273', '2021-09-04 21:31:36.186299', 1);
INSERT INTO public.approver (created_at, updated_at, fk_id_budget, fk_id_approver) VALUES ('2021-09-06 20:55:12.000000', '2021-09-06 20:55:14.000000', 1, 2);
INSERT INTO public.approver (created_at, updated_at, fk_id_budget, fk_id_approver) VALUES ('2021-09-06 20:55:36.000000', '2021-09-06 20:55:37.000000', 2, 2);
INSERT INTO public.approver (created_at, updated_at, fk_id_budget, fk_id_approver) VALUES ('2021-09-06 20:55:45.000000', '2021-09-06 20:55:46.000000', 3, 2);
INSERT INTO public.approver (created_at, updated_at, fk_id_budget, fk_id_approver) VALUES ('2021-09-06 20:55:55.000000', '2021-09-06 20:55:57.000000', 4, 2);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('ARTROSCOPIA', 'CAIXA DE OTICA', '', '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 1);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('CIRURG GERAL', 'ELETROCIRURGIA', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 1);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('CIRURG GERAL', 'UROGINECOLOGIA', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 1);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('MED CHINESA', 'DOR ARTICULACAO', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 1);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('MED CHINESA', 'RESFRIADO', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 1);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('TRAUMA', 'CAIXA DE INSTRUMENTAL', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 1);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('SERVICOS', 'SERVICOS', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 1);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('MED CHINESA', 'RESFRIADO COM FEBRE ALTA', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 2);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('TRAUMA', 'VARILOC 2.7-3.5', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 4);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('TRAUMA', 'PINOS', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 3);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('ARTROSCOPIA', 'EQUIPAMENTOS', '', '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 2);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('CIRURG GERAL', 'INSTRUMENTOS', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 3);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('MED CHINESA', 'OFTALMOLOGIA', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 4);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('MED CHINESA', 'AGULHA PARA ACUPUNTURA', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 2);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('MED CHINESA', 'TONICO', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 3);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('MED CHINESA', 'DERMATOLOGIA', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 3);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('CIRURG GERAL', 'ACESSO', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 4);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('CIRURG GERAL', 'ACESSORIOS', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 5);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('CIRURG GERAL', 'LAPAROSCOPIA', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 4);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('MED CHINESA', 'OTOLOGIA', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 5);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('CIRURG GERAL', 'EQUIPAMENTOS', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 2);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('CIRURG GERAL', 'LIGACAO', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 5);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('TRAUMA', 'FIXADORES ZIMEDE', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 2);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('MED CHINESA', 'DIARREIA', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 4);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('MED CHINESA', 'INSONIA', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 3);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('MED CHINESA', 'DIGESTIVO', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 5);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('TRAUMA', 'VARILOC 2.7-3.5', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 5);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('MED CHINESA', 'GINECOLOGIA', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 2);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('MED CHINESA', 'TOSSE', null, '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 4);
INSERT INTO public.business_unit (name, product_family, description, created_at, updated_at, fk_id_employees) VALUES ('ARTROSCOPIA', 'UROGINECOLOGIA', '', '2021-09-05 12:27:44.000000', '2021-09-05 12:27:46.000000', 3);
INSERT INTO public.status_budget (status, current, message, created_at, updated_at, fk_id_budget) VALUES ('draft', false, 'rascunho', '2021-09-06 13:51:33.615344', '2021-09-06 17:10:52.723253', 1);
INSERT INTO public.status_budget (status, current, message, created_at, updated_at, fk_id_budget) VALUES ('approve', false, 'aprova ai', '2021-09-06 15:23:54.309314', '2021-09-06 17:10:52.723253', 1);
INSERT INTO public.status_budget (status, current, message, created_at, updated_at, fk_id_budget) VALUES ('approved', true, 'ok aprovei', '2021-09-06 17:10:52.757715', '2021-09-06 17:10:52.757755', 1);
INSERT INTO public.months (month, year, value, type, description, comment, created_at, updated_at, fk_id_business_unit, fk_id_budget) VALUES ('january', 2021, 3400.03, 'income', null, null, '2021-09-08 20:12:07.000000', '2021-09-08 20:12:09.000000', 1, 1);
INSERT INTO public.months (month, year, value, type, description, comment, created_at, updated_at, fk_id_business_unit, fk_id_budget) VALUES ('february', 2021, 24433.00, 'income', null, null, '2021-09-08 20:12:10.000000', '2021-09-08 20:12:11.000000', 2, 1);
INSERT INTO public.months (month, year, value, type, description, comment, created_at, updated_at, fk_id_business_unit, fk_id_budget) VALUES ('march', 2021, 3342.00, 'income', null, null, '2021-09-08 20:12:12.000000', '2021-09-08 20:12:13.000000', 3, 1);
INSERT INTO public.months (month, year, value, type, description, comment, created_at, updated_at, fk_id_business_unit, fk_id_budget) VALUES ('april', 2021, 2234.00, 'income', null, null, '2021-09-08 20:12:13.000000', '2021-09-08 20:12:14.000000', 4, 1);
INSERT INTO public.months (month, year, value, type, description, comment, created_at, updated_at, fk_id_business_unit, fk_id_budget) VALUES ('may', 2021, 6544.00, 'income', null, null, '2021-09-08 20:12:07.000000', '2021-09-08 20:12:09.000000', 5, 1);
INSERT INTO public.months (month, year, value, type, description, comment, created_at, updated_at, fk_id_business_unit, fk_id_budget) VALUES ('june', 2021, 3332.00, 'income', null, null, '2021-09-08 20:12:10.000000', '2021-09-08 20:12:11.000000', 6, 1);
INSERT INTO public.months (month, year, value, type, description, comment, created_at, updated_at, fk_id_business_unit, fk_id_budget) VALUES ('july', 2021, 335.20, 'income', null, null, '2021-09-08 20:12:12.000000', '2021-09-08 20:12:13.000000', 7, 1);
INSERT INTO public.months (month, year, value, type, description, comment, created_at, updated_at, fk_id_business_unit, fk_id_budget) VALUES ('august', 2021, 4453.00, 'income', null, null, '2021-09-08 20:12:07.000000', '2021-09-08 20:12:09.000000', 8, 1);
INSERT INTO public.months (month, year, value, type, description, comment, created_at, updated_at, fk_id_business_unit, fk_id_budget) VALUES ('september', 2021, 35333.00, 'income', null, null, '2021-09-08 20:12:07.000000', '2021-09-08 20:12:09.000000', 9, 2);
INSERT INTO public.months (month, year, value, type, description, comment, created_at, updated_at, fk_id_business_unit, fk_id_budget) VALUES ('october', 2021, 56433.00, 'income', null, null, '2021-09-08 20:12:10.000000', '2021-09-08 20:12:11.000000', 12, 3);
INSERT INTO public.months (month, year, value, type, description, comment, created_at, updated_at, fk_id_business_unit, fk_id_budget) VALUES ('november', 2021, 2223.00, 'income', null, null, '2021-09-08 20:12:12.000000', '2021-09-08 20:12:13.000000', 20, 1);
INSERT INTO public.months (month, year, value, type, description, comment, created_at, updated_at, fk_id_business_unit, fk_id_budget) VALUES ('december', 2021, 4433.00, 'income', null, null, '2021-09-08 20:12:13.000000', '2021-09-08 20:12:14.000000', 29, 1);
INSERT INTO public.token (access_token, refresh_token, enable, exp, created_at, updated_at, fk_id_employees) VALUES ('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjp7ImlkIjo1MDEsInN1YiI6ImNhcmxvc0B0YWltaW4uY29tLmJyIiwiZmlyc3RfbmFtZSI6ImNhcmxvcyIsImxhc3RfbmFtZSI6InN0cmluZyIsInBvc2l0aW9uIjoibWFuYWdlciJ9LCJyb2xlIjp7ImlzX2FkbWluIjp0cnVlLCJhY3RpdmUiOnRydWUsImNhbl9zaW11bGF0ZV9idWRnZXQiOnRydWUsImNhbl9zdWJtaXRfYnVkZ2V0Ijp0cnVlLCJjYW5fYXBwcm92ZV9idWRnZXQiOnRydWUsImNhbl9yZWFkX2J1ZGdldCI6dHJ1ZX0sImV4cCI6MTYzMDg2MDEyNX0.7S9QRFRDux5OJP2AxF_uQcauAdqFg9WZwkkNAPet8qQ', 'd22461ba0e5f11ec88771e00d9261241', true, '2021-09-05 16:42:05.189686', '2021-09-05 12:42:05.210431', '2021-09-05 12:42:05.210479', 1);
