FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["DataAccessService/DataAccessService.csproj", "DataAccessService/"]
RUN dotnet restore "DataAccessService/DataAccessService.csproj"
COPY . .
WORKDIR "/src/DataAccessService"
RUN dotnet build "DataAccessService.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "DataAccessService.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "DataAccessService.dll"]
