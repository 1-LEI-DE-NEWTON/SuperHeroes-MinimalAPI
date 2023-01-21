using MinimalAPI;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddDbContext<DataContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

async Task<List<SuperHero>> GetAllHeroes(DataContext context) =>
    await context.SuperHeroes.ToListAsync();

app.MapGet("/", () => "Bem-vindo ao banco de dados de super her�is!");

app.MapGet("/superhero", async (DataContext context) =>
    await context.SuperHeroes.ToListAsync());

app.MapGet("/superhero/{id}", async (DataContext context, int id) =>
    await context.SuperHeroes.FindAsync(id) is SuperHero hero ? 
    Results.Ok(hero) :
    Results.NotFound("Perd�o, super her�i n�o encontrado"));

app.MapPost("/superhero", async (DataContext context, SuperHero hero) =>
{
    context.SuperHeroes.Add(hero);
    await context.SaveChangesAsync();
    return Results.Ok(await GetAllHeroes(context));
});

app.MapPut("/superhero/{id}", async (DataContext context, int id, SuperHero hero) =>
{
    var dbHero = await context.SuperHeroes.FindAsync(id);
    if (dbHero is null)
        return Results.NotFound("Perd�o, super her�i n�o encontrado");

    dbHero.Firstname = hero.Firstname;
    dbHero.Lastname = hero.Lastname;
    dbHero.Heroname = hero.Heroname;
    await context.SaveChangesAsync();
    
    return Results.Ok(await GetAllHeroes(context));
});

app.MapDelete("/superhero/{id}", async (DataContext context, int id) =>
{
    var dbHero = await context.SuperHeroes.FindAsync(id);
    if (dbHero is null)
        return Results.NotFound("Perd�o, super her�i n�o encontrado");

    context.SuperHeroes.Remove(dbHero);
    await context.SaveChangesAsync();
    return Results.Ok(await GetAllHeroes(context));
});

app.Run();