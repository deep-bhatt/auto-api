CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ENUMS
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'field_type_enum') THEN
        CREATE TYPE field_type_enum AS ENUM ('string', 'boolean', 'number');
    END IF;
END
$$;

-- TABLES
CREATE TABLE IF NOT EXISTS public.field (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  field_name VARCHAR(255) UNIQUE,
  field_type field_type_enum,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS public.dataset (
  id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  row_id UUID NOT NULL,
  field_id UUID REFERENCES public.field(id),
  field_value TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
-- CREATE TABLE IF NOT EXISTS public.api (
--   id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
--   field_id UUID REFERENCES public.field(id),
--   name VARCHAR(255) UNIQUE,
--   type VARCHAR(255) DEFAULT 'GET',
--   is_enabled BOOLEAN DEFAULT TRUE,
--   is_auth BOOLEAN DEFAULT FALSE,
--   description text DEFAULT NULL,
--   code_example text DEFAULT NULL,
--   created_at TIMESTAMPTZ DEFAULT NOW()
-- );
