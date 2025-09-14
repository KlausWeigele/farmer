-- Schema v1: core entities and RLS scaffold
create extension if not exists postgis;

create table if not exists farm (
  id uuid primary key default gen_random_uuid(),
  name text not null,
  created_at timestamptz not null default now()
);

create table if not exists app_user (
  id uuid primary key default gen_random_uuid(),
  email text unique not null,
  created_at timestamptz not null default now()
);

create table if not exists membership (
  user_id uuid references app_user(id) on delete cascade,
  farm_id uuid references farm(id) on delete cascade,
  role text not null,
  primary key (user_id, farm_id)
);

create table if not exists field (
  id uuid primary key default gen_random_uuid(),
  farm_id uuid references farm(id) on delete cascade,
  name text,
  area_ha numeric,
  geom geometry(MultiPolygon, 25832) not null,
  created_at timestamptz not null default now()
);

create table if not exists crop_cycle (
  id uuid primary key default gen_random_uuid(),
  field_id uuid references field(id) on delete cascade,
  year int not null,
  crop text,
  variety text,
  created_at timestamptz not null default now()
);

create table if not exists task (
  id uuid primary key default gen_random_uuid(),
  field_id uuid references field(id) on delete cascade,
  type text not null,
  status text not null default 'planned',
  window jsonb,
  due_at timestamptz,
  created_at timestamptz not null default now()
);

create table if not exists operation (
  id uuid primary key default gen_random_uuid(),
  task_id uuid references task(id) on delete set null,
  field_id uuid references field(id) on delete cascade,
  date date not null,
  product text,
  rate_per_ha numeric,
  total_amount numeric,
  weather jsonb,
  notes text,
  created_at timestamptz not null default now()
);

create table if not exists weather_observation (
  id uuid primary key default gen_random_uuid(),
  field_id uuid references field(id) on delete cascade,
  ts timestamptz not null,
  temperature_c numeric,
  wind_ms numeric,
  precipitation_mm numeric,
  humidity_pct numeric
);

create table if not exists ndvi_snapshot (
  id uuid primary key default gen_random_uuid(),
  field_id uuid references field(id) on delete cascade,
  date date not null,
  stats jsonb -- e.g., mean, p10, p90, histogram
);

create table if not exists document (
  id uuid primary key default gen_random_uuid(),
  farm_id uuid references farm(id) on delete cascade,
  kind text,
  object_key text not null,
  ocr_json jsonb,
  created_at timestamptz not null default now()
);

create table if not exists notification (
  id uuid primary key default gen_random_uuid(),
  farm_id uuid references farm(id) on delete cascade,
  payload jsonb,
  created_at timestamptz not null default now()
);

create table if not exists audit_event (
  id uuid primary key default gen_random_uuid(),
  farm_id uuid references farm(id) on delete cascade,
  actor uuid,
  action text,
  details jsonb,
  created_at timestamptz not null default now()
);

-- Note: RLS policies to be added after auth integration

